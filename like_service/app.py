from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.db'
db = SQLAlchemy(app)


class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message_id = db.Column(db.Integer, unique=True)
    like_count = db.Column(db.Integer, default=0)


with app.app_context():
    db.create_all()


@app.route('/like', methods=['POST'])
def like_message():
    data = request.json
    message_id = data.get('message_id')

    like = Like.query.filter_by(message_id=message_id).first()

    if not like:
        like = Like(message_id=message_id, like_count=1)
        db.session.add(like)
    else:
        like.like_count += 1

    db.session.commit()

    return jsonify({'message': 'Message liked', 'likes': like.like_count}), 201


@app.route('/likes/<message_id>', methods=['GET'])
def get_likes(message_id):
    like = Like.query.filter_by(message_id=message_id).first()

    if not like:
        return jsonify({'likes': 0})

    return jsonify({'likes': like.like_count})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
