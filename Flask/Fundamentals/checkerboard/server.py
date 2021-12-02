# Import Flask to allow us to create our app
from flask import Flask, render_template
# Create a new instance of the Flask class called "app"
app = Flask(__name__)


# The "@" decorator associates this route with the function immediately following
@app.route('/')
def chess():
    return render_template("index.html", x=4, y=4, color1="lightblue", color2="yellow")


@app.route('/<int:xnum>')
def chessx(xnum):
    xnum = int(xnum / 2)
    return render_template("index.html", x=xnum, y=4, color1="lightblue", color2="yellow")


@app.route('/<int:xnum>/<int:ynum>')
def chessxy(xnum, ynum):
    xnum = int(xnum / 2)
    ynum = int(ynum / 2)
    return render_template("index.html", x=xnum, y=ynum, color1="lightblue", color2="yellow")


@app.route('/<int:xnum>/<int:ynum>/<string:color1>')
def chessxyc1(xnum, ynum, color1):
    xnum = int(xnum / 2)
    ynum = int(ynum / 2)
    return render_template("index.html", x=xnum, y=ynum, color1=color1, color2="yellow")


@app.route('/<int:xnum>/<int:ynum>/<string:color1>/<string:color2>')
def chessxyc1c2(xnum, ynum, color1, color2):
    xnum = int(xnum / 2)
    ynum = int(ynum / 2)
    return render_template("index.html", x=xnum, y=ynum, color1=color1, color2=color2)

if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
