from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/dojo')
def dojo():
    return 'Dojo!'


@app.route('/say/<string:word>')
def sayhi(word):
    return f"Hi {word}!"


@app.route('/repeat/<int:num>/<string:word>')
def repeatword(num, word):
    return f"{word * num}"


@app.route('/<error>')
def hallmonitor(error):
    return "Sorry! No response. Try again."

if __name__ == "__main__":
    app.run(debug=True)
