from flask import Flask, render_template, request, redirect
# import the class from friend.py
from user import User
app = Flask(__name__)


@app.route('/user')
def index():
    users = User.get_all()
    print(users)
    return render_template("read.html", all_users=users)


@app.route('/user/new')
def usernew():
    pass
    return render_template("create.html")


@app.route('/user/new/create', methods=["POST"])
def create_user():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "em": request.form["em"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    User.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/user')

if __name__ == "__main__":
    app.run(debug=True)
