from flask import Flask, request, jsonify
from filters.text_filter import apply_text_filter
from filters.screaming_filter import apply_screaming
from filters.publish_filter import apply_publishing

app = Flask(__name__)


def process_message(message):
    # sequential application
    filtered_message = apply_text_filter(message)
    if filtered_message is None:
        return

    screamed_message = apply_screaming(filtered_message)
    result = apply_publishing(screamed_message)

    return result


@app.route('/submit_message', methods=['POST'])
def submit_message():
    # Input validation
    data = request.get_json()
    if not data or 'alias' not in data or 'text' not in data:
        return jsonify({'error': 'Invalid data'}), 400
    message = {
        'alias': data['alias'],
        'text': data['text']
    }

    status = process_message(message)
    if status:
        return jsonify({'status': 'ok'}), 200
    else:
        return jsonify({'status': 'error'}), 400


if __name__ == '__main__':
    app.run(debug=True)
