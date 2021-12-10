from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import connectToMySQL

app = Flask(__name__)
app.secret_key = 'dojosurvey'


@app.route('/')
def surveypage():
    return render_template("index.html")


@app.route('/process', methods=['POST'])
def process():
    if not validate_form(request.form):
        return redirect('/')

    data = {
        "name": request.form['name'],
        "location": request.form['location'],
        "language": request.form['language'],
        "comment": request.form['comment']
    }
    save(data)
    return redirect('/result')


@app.route('/result')
def result():
    return render_template("result.html", info=session)

def save(data):
    query = "INSERT INTO dojos (name, location, language, comment, created_at,updated_at) VALUES (%(name)s,%(location)s,%(language)s,%(comment)s,NOW(),NOW())"
    return connectToMySQL('survey').query_db(query, data)

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
