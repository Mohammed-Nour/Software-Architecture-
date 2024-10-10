from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.db'
db = SQLAlchemy(app)

MAX_MESSAGES = 10
USER_SERVICE_URL = 'http://user_service:5000'


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    content = db.Column(db.String(500))


with app.app_context():
    db.create_all()


@app.route('/post', methods=['POST'])
def post_message():
    data = request.json
    username = data.get('username')
    content = data.get('content')

    if not username or not content:
        return jsonify({'error': 'Username and content are required'}), 400

    response = requests.get(f'{USER_SERVICE_URL}/users/{username}')
    if response.status_code != 200:
        return jsonify({'error': 'User not found'}), 404

    if len(content) > 400:
        return jsonify({'error': 'Message too long'}), 400

    # Create the message with a unique ID
    new_message = Message(username=username, content=content)
    db.session.add(new_message)

    # Keep only the last MAX_MESSAGES
    all_messages = Message.query.all()
    if len(all_messages) > MAX_MESSAGES:
        db.session.delete(all_messages[0])

    db.session.commit()

    return jsonify({'message': 'Message posted successfully', 'message_id': new_message.id}), 201


# In this function we retrieve the last message
@app.route('/feed', methods=['GET'])
def get_feed():
    latest_messages = Message.query.order_by(Message.id.desc()).limit(MAX_MESSAGES).all()
    feed = [{'id': message.id, 'username': message.username, 'content': message.content} for message in latest_messages]

    return jsonify(feed)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
