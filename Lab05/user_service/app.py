from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)


with app.app_context():
    db.create_all()


@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')

    if not username:
        return jsonify({'error': 'Username is required'}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'Username already exists'}), 409

    new_user = User(username=username)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201


@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    user = User.query.filter_by(username=username).first()

    if not user:
        return jsonify({'error': 'User not found'}), 404

    return jsonify({'username': user.username})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
