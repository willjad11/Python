from flask_app import app
from flask_bcrypt import Bcrypt
from flask_app import app
from flask import render_template, redirect, flash, request, session
from flask_app.models.user import User
from flask_app.models.message import Message
import datetime

bcrypt = Bcrypt(app)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/wall')
def wall():
    if 'user_id' not in session:
        return redirect("/")
    userid = session['user_id']
    firstname = session['first_name']
    lastname = session['last_name']
    loggedin = session['logged_in']
    users = User.get_all_users()
    messages = Message.get_all_messages({"id": userid})
    count = Message.message_count({"id": userid})
    return render_template("wall.html", userid=userid, firstname=firstname, lastname=lastname, loggedin=loggedin, messages=messages, users=users, count=count)

@app.route('/login', methods=['POST'])
def login():
    user_in_db = User.get_by_email({"em": request.form["em"]})
    if not user_in_db:
        flash("Invalid Email/Password", 'login')
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['pas']):
        flash("Invalid Email/Password", 'login')
        return redirect('/')
    session['user_id'] = user_in_db.id
    session['first_name'] = user_in_db.first_name
    session['last_name'] = user_in_db.last_name
    session['logged_in'] = True
    return redirect("/wall")


@app.route('/logout', methods=['POST'])
def logout():
    if int(request.form['id']) == int(session['user_id']):
        session.clear()
    return redirect("/")

@app.route('/register', methods=['POST'])
def register():
    if len(request.form['fname']) < 3:
        flash("First name must be at least 3 characters in length.", 'register1')
        return redirect('/')
    if len(request.form['lname']) < 3:
        flash("Last name must be at least 3 characters in length.", 'register2')
        return redirect('/')
    if not User.validate_email(request.form):
        flash("Invalid email address!", 'register3')
        return redirect('/')
    if not User.validate_pass(request.form['pas']):
        flash("Password must be minimum eight characters, at least one uppercase letter, one lowercase letter, one number and one special character!", 'register4')
        return redirect('/')
    if request.form['pas'] != request.form['cpas']:
        flash("Passwords do not match!", 'register4')
        return redirect('/')
    data = {
        "em": request.form['em']
    }
    if User.is_duplicate(data):
        flash("Email is already registered with another account.", 'register3')
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['pas'])
    print(pw_hash)
    data = {
        "fname": request.form['fname'],
        "lname": request.form['lname'],
        "em": request.form['em'],
        "pas": pw_hash
    }
    user_id = User.register(data)
    session['user_id'] = user_id
    session['first_name'] = User.get_by_id({"id": user_id}).first_name
    session['last_name'] = User.get_by_id({"id": user_id}).last_name
    session['logged_in'] = True
    return redirect("/wall")
