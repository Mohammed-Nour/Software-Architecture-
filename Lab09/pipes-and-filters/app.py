import os
import smtplib
import configparser
from email.message import EmailMessage
import multiprocessing
from flask import Flask, request, jsonify
import json

# Path to config.ini file
script_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(script_dir, 'config.ini')

# Print current working directory to help with path issues
print(f"Current working directory: {os.getcwd()}")

# RabbitMQ connection settings
RABBITMQ_HOST = "rabbitmq"
QUEUE_NAME = "publish_queue"

# Load SMTP credentials from config file
config = configparser.ConfigParser()

# Check if config file exists
if os.path.exists(config_path):
    print(f"Config file found at {config_path}")
    config.read(config_path)
else:
    print(f"Config file not found at {config_path}")

# Check if the 'SMTP' section exists in the config file
if 'SMTP' in config:
    print("SMTP section found!")
else:
    print("SMTP section not found in the config file.")

# Fetch the email and password from the config file
try:
    EMAIL_ADDRESS = config['SMTP']['email_address']
    EMAIL_PASSWORD = config['SMTP']['email_password']
    print(f"Loaded email address: {EMAIL_ADDRESS}")
except KeyError as e:
    print(f"Error: Missing configuration for {e}")

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
STOP_WORDS = ["bird-watching", "ailurophobia", "mango"]

def contains_stop_words(text):
    """
    Check if the text contains any of the stop words.
    """
    return any(word in text.lower() for word in STOP_WORDS)


def send_email(message):
    """
    Sends an email with the given message.
    """
    try:
        print(f"Connecting to SMTP server {SMTP_SERVER} on port {SMTP_PORT}...")
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade to secure connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            email = EmailMessage()
            email["From"] = EMAIL_ADDRESS
            email["To"] = ["yehiasobeh3@gmail.com"]  # Replace with your recipient(s)
            email["Subject"] = "New Message from Publish Service"
            email.set_content(message)
            
            server.send_message(email)
            print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")


def api_service(api_pipe, filter_input_pipe):
    """
    The API service receives data from the Flask API and forwards it to the filter service.
    """
    print("[API Service] Starting...")
    while True:
        try:
            data = api_pipe.recv()  # Blocking call
            print(f"[API Service] Received data: {data}")

            # Forward the data to the filter service
            filter_input_pipe.send(data)

        except KeyboardInterrupt:
            print("[API Service] Terminated.")
            break


def filter_service(input_pipe, output_pipe):
    """
    The filter service receives data from API service, processes it, and forwards or drops it.
    """
    print("[Filter Service] Starting...")
    while True:
        try:
            data = input_pipe.recv()  # Blocking call
            print(f"[Filter Service] Received data: {data}")

            # Check for stop words
            if contains_stop_words(data['text']):
                print(f"[Filter Service] Message contains stop words and will be dropped: {data['text']}")
            else:
                print(f"[Filter Service] Message passed the filter and will be forwarded.")
                # Forward the message to the next process
                output_pipe.send(data)
                print("[Filter Service] Forwarded data to Screaming Service")
        except KeyboardInterrupt:
            print("[Filter Service] Terminated.")
            break


def screaming_service(screaming_pipe, publish_input_pipe):
    """
    The screaming service processes the data (converts to uppercase) and forwards it to the publish service.
    """
    print("[Screaming Service] Starting...")
    while True:
        try:
            data = screaming_pipe.recv()  # Blocking call
            print(f"[Screaming Service] Received data: {data}")

            # Convert text to uppercase
            data['text'] = data['text'].upper()

            # Forward the data to the publish service
            publish_input_pipe.send(data)

        except KeyboardInterrupt:
            print("[Screaming Service] Terminated.")
            break


def publish_service(input_pipe, output_pipe):
    """
    The publish service consumes messages from the queue, processes them, and sends email notifications.
    """
    print("[Publish Service] Starting...")
    while True:
        try:
            # Receive data from the previous process (Screaming Process)
            data = input_pipe.recv()  # Blocking call
            print(f"[Publish Service] Received data: {data}")

            # Send the processed message via email
            send_email(data['text'])

            # Optionally, you can do further actions with the data, e.g., log it, save it, etc.
            print("[Publish Service] Email sent with message.")

        except KeyboardInterrupt:
            print("[Publish Service] Terminated.")
            break


# Flask app to receive POST requests
app = Flask(__name__)

# Create pipes for communication between processes
api_pipe, api_input_pipe = multiprocessing.Pipe()
filter_pipe, filter_input_pipe = multiprocessing.Pipe()
screaming_pipe, screaming_input_pipe = multiprocessing.Pipe()
publish_pipe, publish_input_pipe = multiprocessing.Pipe()

# API route to handle client POST requests
@app.route('/submit_message', methods=['POST'])
def handle_post_request():
    try:
        data = request.get_json()  # Get data from the POST request
        print(f"[Flask] Received POST data: {data}")

        # Send received data to the API process pipe to start the chain
        api_input_pipe.send(data)

        return jsonify({"message": "Data received and processing started."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == '__main__':
    print("[Main] Starting all processes...")

    # Start the four processes
    api_process = multiprocessing.Process(target=api_service, args=(api_pipe, filter_input_pipe))
    filter_process = multiprocessing.Process(target=filter_service, args=(filter_pipe, screaming_input_pipe))
    screaming_process = multiprocessing.Process(target=screaming_service, args=(screaming_pipe, publish_input_pipe))
    publish_process = multiprocessing.Process(target=publish_service, args=(publish_pipe, None))

    api_process.start()
    filter_process.start()
    screaming_process.start()
    publish_process.start()

    # Start Flask app
    app.run(host="0.0.0.0", port=6000,debug=False, use_reloader=False)  # Flask runs the web server

    # Optionally, wait for processes to terminate when the Flask app ends
    api_process.join()
    filter_process.join()
    screaming_process.join()
    publish_process.join()
