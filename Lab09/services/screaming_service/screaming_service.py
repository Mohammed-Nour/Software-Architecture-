import pika
import json

RABBITMQ_HOST = "localhost"
INPUT_QUEUE = "filtered_queue"
OUTPUT_QUEUE = "publish_queue"


def callback(ch, method, properties, body):
    message = json.loads(body)
    print(f"SCREAMING Service: Received message: {message}")

    message['text'] = message['text'].upper()
    print(f"SCREAMING Service: Converted message to uppercase: {message}")

    ch.basic_publish(exchange="", routing_key=OUTPUT_QUEUE, body=json.dumps(message))
    ch.basic_ack(delivery_tag=method.delivery_tag)


def start_screaming_service():
    print("Connecting to RabbitMQ...")
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
    channel = connection.channel()

    channel.queue_declare(queue=INPUT_QUEUE, durable=True)
    channel.queue_declare(queue=OUTPUT_QUEUE, durable=True)

    print(f"SCREAMING service is running and listening on queue: {INPUT_QUEUE}")
    channel.basic_consume(queue=INPUT_QUEUE, on_message_callback=callback)

    channel.start_consuming()


if __name__ == "__main__":
    try:
        start_screaming_service()
    except KeyboardInterrupt:
        print("SCREAMING service stopped manually.")
    except Exception as e:
        print(f"Error in SCREAMING Service: {e}")
