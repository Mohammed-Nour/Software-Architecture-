STOP_WORDS = ["bird-watching", "ailurophobia", "mango"]


def apply_text_filter(message):
    if any(word in message['text'].lower() for word in STOP_WORDS):
        print(f"Filter Service: Message contains stop words and will be dropped: {message['text']}")
        return None

    print(f"Filter Service: Message passed the filter and will be forwarded.")
    return message
