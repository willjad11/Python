from flask_app import app
from flask_bcrypt import Bcrypt
from flask_app import app
from flask import render_template, redirect, flash, request, session
from flask_app.models.user import User
from flask_app.models.recipe import Recipe

bcrypt = Bcrypt(app)


@app.route('/')
def index():
    if 'user_id' in session:
        return redirect("/dashboard")
    return render_template("index.html")


@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect("/")
    return render_template("dashboard.html", userid=session['user_id'], firstname=session['first_name'], recipes=Recipe.get_all())

@app.route('/login', methods=['POST'])
def login():
    if 'user_id' in session:
        redirect("/dashboard")
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
    return redirect("/dashboard")


@app.route('/logout', methods=['POST'])
def logout():
    if int(request.form['id']) == int(session['user_id']):
        session.clear()
    return redirect("/")

@app.route('/register', methods=['POST'])
def register():
    if len(request.form['fname']) < 2:
        flash("First name must be at least 2 characters in length.", 'register1')
        return redirect('/')
    if len(request.form['lname']) < 2:
        flash("Last name must be at least 2 characters in length.", 'register2')
        return redirect('/')
    if not User.validate_email(request.form):
        flash("Invalid email address!", 'register3')
        return redirect('/')
    if User.is_duplicate({"em": request.form['em']}):
        flash("Email is already registered with another account.", 'register3')
        return redirect('/')
    if not User.validate_pass(request.form['pas']):
        flash("Password must be minimum eight characters, at least one uppercase letter, one lowercase letter, one number and one special character!", 'register4')
        return redirect('/')
    if request.form['pas'] != request.form['cpas']:
        flash("Passwords do not match!", 'register4')
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['pas'])
    user_id = User.register({
        "fname": request.form['fname'],
        "lname": request.form['lname'],
        "em": request.form['em'],
        "pas": pw_hash
    })
    session['user_id'] = user_id
    session['first_name'] = User.get_by_id({"id": user_id}).first_name
    session['last_name'] = User.get_by_id({"id": user_id}).last_name
    session['logged_in'] = True
    return redirect("/dashboard")
