from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')

    if not username:
        return jsonify({'error': 'Username is required'}), 400

    if username in users:
        return jsonify({'error': 'Username already exists'}), 409

    users[username] = {'username': username}
    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    if username not in users:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(users[username])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
