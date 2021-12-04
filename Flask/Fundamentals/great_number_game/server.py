from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'great'



@app.route('/')
def numbergame():
    if 'guesses' not in session:
        session['guesses'] = 0
    if 'guessesleft' not in session:
        session['guessesleft'] = 5
    if 'won' not in session:
        session['won'] = False
    if 'rannum' not in session:
        session['rannum'] = random.randint(0, 100)
    if 'loworhigh' not in session:
        session['loworhigh'] = 1
    print(session['rannum'])
    return render_template("index.html", guesses=session['guesses'], guessesleft=session['guessesleft'], won=session['won'], rannum=session['rannum'], loworhigh=session['loworhigh'])


@app.route('/guess', methods=['POST'])
def guess():
    if session['guessesleft'] > 0:
        session['guessesleft'] -= 1
        session['guesses'] += 1
        if int(request.form['guess']) < session['rannum']:
            session['loworhigh'] = 2 #loworhigh is 2 if guess is less than number
        elif int(request.form['guess']) > session['rannum']:
            session['loworhigh'] = 3 #loworhigh is 3 if guess is less than number
        elif int(request.form['guess']) == session['rannum'] and session['guessesleft'] == 0:
            session['loworhigh'] = 1 #return loworhigh to 1 since correct number is guessed
            session['won'] = True #set lostorwon to 2 when we win
        elif int(request.form['guess']) == session['rannum']:
            session['loworhigh'] = 1 #return loworhigh to 1 since correct number is guessed
            session['won'] = True #set lostorwon to 2 when we win
    elif int(session['guessesleft']) == 0:
        session['won'] = False
    return render_template("index.html", guesses=session['guesses'], guessesleft=session['guessesleft'], won=session['won'], rannum=session['rannum'], loworhigh=session['loworhigh'])


@app.route('/playagain', methods=['GET'])
def playagain():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
