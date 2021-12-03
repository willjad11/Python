from flask import Flask, render_template, request, redirect, session
from users import UserDatabase

app = Flask(__name__)
app.secret_key = 'testkey'

userdata = UserDatabase()

loggedin = False

@app.route('/')
def index():
    if "session['username']" not in locals():
        userauth = "None"
        loggedin = False
    else:
        userauth = session['username']
        loggedin = True
    return render_template("index.html", userauth=userauth, error=userdata.error, errormsg=userdata.errormsg, loggedin=loggedin)


@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    userdata.data[request.form['username']] = [[request.form['password'], 0]]
    print(userdata.data)
    return redirect('/')


@app.route('/login', methods=['POST'])
def login():
    if request.form['username'] in userdata.data.keys():
        print("Found username in keys")
        if request.form['password'] == userdata.data[request.form['username']][0][0]:
            print("Password is true")
            userdata.error = False
            userdata.errormsg = ""
            userdata.data[request.form['username']][0][1] = 1
            session['username'] = request.form['username']
        elif request.form['password'] != userdata.data[request.form['username']][0][0]:
            print("Wrong login info")
            userdata.error = True
            userdata.errormsg = "Wrong login"
    else:
        print("Wrong login info")
        userdata.error = True
        userdata.errormsg = "Wrong login"
    return redirect('/')


@app.route('/logout', methods=['POST'])
def logout():
    print("User logged out")
    userdata.data[session['username']][0][1] = 0
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

