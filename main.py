from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chat.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    sender_id = db.Column(db.Integer)
    receiver_id = db.Column(db.Integer)

    text = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

def send_message(sender, receiver, text):
    msg = Message(
        sender_id=sender,
        receiver_id=receiver,
        text=text
    )

    db.session.add(msg)
    db.session.commit()

with app.app_context():
    db.create_all()

    send_message(1, 2, "Hello bro!")
    send_message(2, 1, "Salom 😎")

    messages = Message.query.all()

    for m in messages:
        print(m.text)
