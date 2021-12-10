from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.email import Email

@app.route('/')
def email_index():
    return render_template("index.html")


@app.route('/addemail', methods=['POST'])
def add_email():
    if not Email.validate_email(request.form):
        return redirect('/')
    session['email'] = request.form['email']
    data = {
        "email": request.form['email']
    }
    if Email.is_duplicate(data):
        return redirect('/')
    Email.save(data)
    return redirect("/show")


@app.route('/show')
def show_index():
    emails = Email.get_all()
    return render_template("success.html", emails=emails, myemail=session['email'])
