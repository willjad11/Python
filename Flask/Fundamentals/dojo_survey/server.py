from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'dojosurvey'


@app.route('/')
def surveypage():
    return render_template("index.html")


@app.route('/process', methods=['POST'])
def process():
    if not validate_form(request.form):
        return redirect('/')
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/result')


@app.route('/result')
def result():
    return render_template("result.html", info=session)


@staticmethod
def validate_form(form):
    is_valid = True
    if len(form['name']) < 2:
        flash("Name must be at least 2 characters.")
        is_valid = False
    if len(form['location']) < 7:
        flash("Please select a valid location.")
        is_valid = False
    if len(form['language']) < 4:
        flash("Please select a valid language.")
        is_valid = False
    if len(form['comment']) > 250:
        flash("Your comment is too long. 250 characters maximum.")
        is_valid = False
    return is_valid

if __name__ == "__main__":
    app.run(debug=True)
