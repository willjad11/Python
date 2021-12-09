# burgers.py
from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.friend import Friend


@app.route('/')
def index():
    friends = Friend.get_all()
    print(friends)
    return render_template("index.html", all_friends=friends)


@app.route('/create_friend', methods=["POST"])
def create_friend():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "occ": request.form["occ"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    Friend.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/')


@app.route('/delete_friend', methods=["POST"])
def delete_friend():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "fid": request.form["fid"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    Friend.delete(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/')
