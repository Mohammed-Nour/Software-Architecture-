def apply_screaming(message):
    print(f"SCREAMING Service: Received message: {message}")

    message['text'] = message['text'].upper()
    print(f"SCREAMING Service: Converted message to uppercase: {message}")

    return message
