# user_api_service.py
from flask import Flask, request, jsonify
import pika
import json

app = Flask(__name__)


def publish_message(message):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    print("Connected to RabbitMQ!")

    channel = connection.channel()
    channel.queue_declare(queue='user_queue', durable=True)
    channel.basic_publish(
        exchange='',
        routing_key='user_queue',
        body=json.dumps(message),
        properties=pika.BasicProperties(delivery_mode=2)  # make message persistent
    )
    connection.close()


@app.route('/submit_message', methods=['POST'])
def submit_message():
    data = request.get_json()
    if not data or 'alias' not in data or 'text' not in data:
        return jsonify({'error': 'Invalid data'}), 400

    message = {
        'alias': data['alias'],
        'text': data['text']
    }
    publish_message(message)
    return jsonify({'status': 'Message received'}), 200


if __name__ == '__main__':
    app.run(debug=True)
