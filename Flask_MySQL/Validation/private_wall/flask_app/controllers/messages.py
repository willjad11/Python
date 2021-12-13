from flask_app import app
from flask_app import app
from flask import render_template, redirect, flash, request, session
from flask_app.models.message import Message


@app.route('/sendmessage', methods=['POST'])
def send_message():
    if 'user_id' not in session:
        redirect('/')
    if len(request.form['msg']) < 10:
        flash("Message too short! Must be at least 5 characters", "sendmsg2")
        return redirect("/wall")
    data = {
        "sid": session['user_id'],
        "rid": request.form["rid"], 
        "msg": request.form["msg"]
    }
    Message.send_message(data)
    flash("Your message was sent!", "sendmsg")
    return redirect("/wall")


@app.route('/deletemessage', methods=['POST'])
def delete_message():
    data = {
        "rid": request.form["rid"],
        "mid": request.form["mid"]
    }
    if int(request.form['rid']) != int(session['user_id']):
        redirect('/stop')
    if not Message.verify_message(data):
        redirect('/stop')
    Message.delete_message(data)
    return redirect('/wall')

@app.route('/stop', methods=['POST'])
def stop():
    return render_template("stop.html")
