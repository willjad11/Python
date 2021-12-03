from flask import Flask, render_template, request, redirect # added request
from users import UserDatabase

app = Flask(__name__)

userdata = UserDatabase()

@app.route('/')
def index():
    return render_template("index.html", loggedin = userdata.loggedin, error = userdata.error, errormsg = userdata.errormsg)


@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    userdata.data[request.form['username']] = request.form['password']
    print(userdata.data)
    return redirect('/')


@app.route('/login', methods=['POST'])
def login():
    if request.form['username'] in userdata.data:
        if request.form['username'] == userdata.data.get(request.form['password']):
            print("Got Login Info")
            userdata.error = False
            userdata.errormsg = ""
            userdata.loggedin = True
        if request.form['username'] != userdata.data.get(request.form['password']):
            print("Wrong login info")
            userdata.error = True
            userdata.errormsg = "Wrong login"
    else:
        userdata.error = True
        userdata.errormsg = "Wrong login"
    return redirect('/')


@app.route('/logout', methods=['POST'])
def logout():
    print("User logged out")
    userdata.loggedin = False
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

