from flask import Flask, render_template  # Import Flask to allow us to create our app
# Create a new instance of the Flask class called "app"
app = Flask(__name__)


# The "@" decorator associates this route with the function immediately following
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/hello/<string:banana>/<int:num>')
def hello(banana, num):
    return render_template("hello.html", banana = banana, num = num)

if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
