import pika
import json

# RabbitMQ connection settings
RABBITMQ_HOST = "rabbitmq"
INPUT_QUEUE = "user_queue"
FILTERED_QUEUE = "filtered_queue"

# Stop words to filter
STOP_WORDS = ["bird-watching", "ailurophobia", "mango"]

def contains_stop_words(text):
    """
    Check if the text contains any of the stop words.
    """
    return any(word in text.lower() for word in STOP_WORDS)

def callback(ch, method, properties, body):
    """
    Callback function to process messages from the input queue.
    """
    message = json.loads(body)
    print(f"Filter Service: Received message: {message}")  # Added print statement

    if contains_stop_words(message['text']):
        print(f"Filter Service: Message contains stop words and will be dropped: {message['text']}")
    else:
        print(f"Filter Service: Message passed the filter and will be forwarded.")
        ch.basic_publish(
            exchange="",
            routing_key=FILTERED_QUEUE,
            body=json.dumps(message)
        )
    ch.basic_ack(delivery_tag=method.delivery_tag)

def start_filter_service():
    """
    Starts the Filter Service to consume messages from RabbitMQ.
    """
    print("Connecting to RabbitMQ...")
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
    channel = connection.channel()

    # Declare queues
    channel.queue_declare(queue=INPUT_QUEUE, durable=True)
    channel.queue_declare(queue=FILTERED_QUEUE, durable=True)

    print(f"Filter service is running and listening on queue: {INPUT_QUEUE}")
    channel.basic_consume(queue=INPUT_QUEUE, on_message_callback=callback)

    # Start consuming messages
    channel.start_consuming()

if __name__ == "__main__":
    try:
        start_filter_service()
    except KeyboardInterrupt:
        print("Filter service stopped manually.")
    except Exception as e:
        print(f"Error in Filter Service: {e}")
