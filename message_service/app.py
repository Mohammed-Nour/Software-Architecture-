from flask import Flask, jsonify, request
import requests

app = Flask(__name__)
messages = []
MAX_MESSAGES = 10
current_message_id = 1  # To track message IDs

USER_SERVICE_URL = 'http://user_service:5000'

@app.route('/post', methods=['POST'])
def post_message():
    global current_message_id
    data = request.json
    username = data.get('username')
    content = data.get('content')

    if not username or not content:
        return jsonify({'error': 'Username and content are required'}), 400

    # Check if the user exists
    response = requests.get(f'{USER_SERVICE_URL}/users/{username}')
    if response.status_code != 200:
        return jsonify({'error': 'User not found'}), 404

    if len(content) > 400:
        return jsonify({'error': 'Message too long'}), 400

    # Create the message with a unique ID
    message = {'id': current_message_id, 'username': username, 'content': content}
    messages.append(message)
    
    if len(messages) > MAX_MESSAGES:
        messages.pop(0)  # Keep only the last 10 messages

    current_message_id += 1  # Increment the message ID for the next message

    return jsonify({'message': 'Message posted successfully', 'message_id': message['id']}), 201

@app.route('/feed', methods=['GET'])
def get_feed():
    return jsonify(messages[-MAX_MESSAGES:])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

