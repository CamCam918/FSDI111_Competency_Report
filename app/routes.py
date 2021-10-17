from flask import request, render_template
from app import app, db
from app.database import Message



@app.route("/messages", method=["POST"])
def create_message():
    msg_data = request.json
    title= msg_data.get("title")
    body= msg_data.get("body")
    if not title or not body:
        return "<h1>Invalisd syntax<?h1>", 400
    message = Message(title=title, body = body)
    db.session.add(message)
    db.session.commit()
    return "<h1>Created</h1>", 201

@app.get("/messages")
def read_all_messages():
    return Message.query.all()

@app.get("/messages/<int:pk>")
def read_message_by_id(pk):
    return Message.query.filter_by(id=pk).first()


@app.get("greeting/<name>")
def greet(name):
    return render_template("home.html", name=name)
#implement the following operations:
#1. create message
#2. Scan (display all mesages)
#3. Read single Message (by its ID).
