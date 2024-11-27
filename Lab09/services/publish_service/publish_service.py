import pika
import smtplib
from email.message import EmailMessage

# RabbitMQ connection settings
RABBITMQ_HOST = "localhost"
QUEUE_NAME = "publish_queue"

# SMTP server settings
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "yehiasobeh@gmail.com"  # Replace with your email
EMAIL_PASSWORD = ""  # Replace with your email app password


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
            email["To"] = ["yehiasobeh2@gmail.com"]  # Replace with your recipient(s)
            email["Subject"] = "New Message from Publish Service"
            email.set_content(message)

            server.send_message(email)
            print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")


def callback(ch, method, properties, body):
    """
    Callback function to process messages from the queue.
    """
    print(f"Received message: {body.decode()}")
    send_email(body.decode())
    ch.basic_ack(delivery_tag=method.delivery_tag)  # Acknowledge the message


def start_publish_service():
    """
    Starts the Publish Service to consume messages from RabbitMQ.
    """
    print("Connecting to RabbitMQ...")
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
    channel = connection.channel()

    # Declare the queue (it should match the queue name used by the SCREAMING service)
    channel.queue_declare(queue=QUEUE_NAME, durable=True)

    print(f"Publish service is running and listening on queue: {QUEUE_NAME}")
    channel.basic_consume(queue=QUEUE_NAME, on_message_callback=callback)

    # Start consuming messages
    channel.start_consuming()


if __name__ == "__main__":
    try:
        start_publish_service()
    except KeyboardInterrupt:
        print("Publish service stopped manually.")
    except Exception as e:
        print(f"Error in Publish Service: {e}")
