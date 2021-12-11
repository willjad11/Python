from flask_app import app
from flask_bcrypt import Bcrypt
from flask_app import app
from flask import render_template, redirect, flash, request, session
from flask_app.models.user import User

bcrypt = Bcrypt(app)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/success')
def success():
    if 'user_id' not in session:
        return redirect("/")
    userid = session['user_id']
    firstname = session['first_name']
    lastname = session['last_name']
    loggedin = session['logged_in']
    return render_template("success.html", userid=userid, firstname=firstname, lastname=lastname, loggedin=loggedin)

@app.route('/login', methods=['POST'])
def login():
    # see if the username provided exists in the database
    data = {
        "em": request.form["em"]
        }
    user_in_db = User.get_by_email(data)
    # user is not registered in the db
    if not user_in_db:
        flash("Invalid Email/Password", 'login')
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['pas']):
        # if we get False after checking the password
        flash("Invalid Email/Password", 'login')
        return redirect('/')
    # if the passwords matched, we set the user_id into session
    session['user_id'] = user_in_db.id
    session['first_name'] = user_in_db.first_name
    session['last_name'] = user_in_db.last_name
    session['logged_in'] = True
    # never render on a post!!!
    return redirect("/success")


@app.route('/logout', methods=['POST'])
def logout():
    if int(request.form['id']) == int(session['user_id']):
        session.clear()
    return redirect("/")

@app.route('/register', methods=['POST'])
def register():
    # validate the form here ...
    # create the hash
    if len(request.form['fname']) < 3:
        flash("First name must be at least 3 characters in length.", 'register')
        return redirect('/')
    if len(request.form['lname']) < 3:
        flash("Last name must be at least 3 characters in length.", 'register')
        return redirect('/')
    if not User.validate_email(request.form):
        flash("Invalid email address!", 'register')
        return redirect('/')
    if not User.validate_pass(request.form['pas']):
        flash("Password must be minimum eight characters, at least one uppercase letter, one lowercase letter, one number and one special character!", 'register')
        return redirect('/')
    if request.form['pas'] != request.form['cpas']:
        flash("Passwords do not match!", 'register')
        return redirect('/')
    data = {
        "em": request.form['em']
    }
    if User.is_duplicate(data):
        flash("Email is already registered with another account.", 'register')
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['pas'])
    print(pw_hash)
    # put the pw_hash into the data dictionary
    data = {
        "fname": request.form['fname'],
        "lname": request.form['lname'],
        "em": request.form['em'],
        "pas": pw_hash
    }
    # Call the save @classmethod on User
    user_id = User.register(data)
    # store user id into session
    session['user_id'] = user_id
    session['first_name'] = User.get_by_id({"id": user_id}).first_name
    session['last_name'] = User.get_by_id({"id": user_id}).last_name
    session['logged_in'] = True
    return redirect("/success")
