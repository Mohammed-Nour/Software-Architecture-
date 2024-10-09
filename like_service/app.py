from flask import Flask, jsonify, request

app = Flask(__name__)
likes = {}

@app.route('/like', methods=['POST'])
def like_message():
    data = request.json
    message_id = data.get('message_id')

    if message_id not in likes:
        likes[message_id] = 0

    likes[message_id] += 1
    return jsonify({'message': 'Message liked', 'likes': likes[message_id]}), 201

@app.route('/likes/<message_id>', methods=['GET'])
def get_likes(message_id):
    if message_id not in likes:
        return jsonify({'likes': 0})
    return jsonify({'likes': likes[message_id]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
