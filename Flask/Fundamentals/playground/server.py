from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "hi"


@app.route('/play')
def playground():
    return render_template("playground.html", num = 3, color="lightblue")

@app.route('/play/<int:num>')
def dynamicplayground(num):
    return render_template("playground.html", num = num, color = "lightblue")

@app.route('/play/<int:num>/<string:color>')
def dynamiccolorplayground(num, color):
    return render_template("playground.html", num = num, color = color)


if __name__ == "__main__":
    app.run(debug=True)
