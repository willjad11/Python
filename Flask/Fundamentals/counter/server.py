from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'clickercount'

@app.route('/')
def countpage():
    if 'clicks' in session and 'views' in session:
        print('keys exist!')
        print(session['clicks'])
        session['views'] += 1
    else:
        print("key 'key_name' does NOT exist")
        session['clicks'] = 0
        session['views'] = 1

    return render_template("index.html", viewnum=session['views'], clicks=session['clicks'])
    

@app.route('/click', methods=['POST'])
def incrementcounter():
    if request.form['number'] == "":
        session['clicks'] += 1
        session['views'] -= 1
    else:
        session['views'] += int(request.form['number']) - 1
    return redirect('/')


@app.route('/destroysession', methods=['POST'])
def destroycountpage():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
