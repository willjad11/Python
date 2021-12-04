from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'ninjagold'


class Player:
    def __init__(self):
        pass
    gold = 0
    activities = []


@app.route('/')
def index():
    return render_template("index.html", gold=Player.gold, activities=Player.activities)


@app.route('/process_money', methods=['POST'])
def process_money():
    print(request.form)
    farmgold = random.randint(10, 20)
    cavegold = random.randint(5, 10)
    housegold = random.randint(2, 5)
    casinogold = random.randint(0, 50)
    chance = random.randint(0, 10)
    lostmoney = False
    if "farm" in request.form:
        Player.gold += farmgold
        Player.activities.append(f"Earned {farmgold} golds from farm")
    elif "cave" in request.form:
        Player.gold += cavegold
        Player.activities.append(f"Earned {cavegold} golds from cave")
    elif "house" in request.form:
        Player.gold += housegold
        Player.activities.append(f"Earned {housegold} golds from house")
    elif "casino" in request.form:
        if chance > 5:
            if Player.gold - casinogold < 0:
                lostmoney = True
                Player.gold = 0
                Player.activities.append(f"Lost {casinogold} golds from casino")
            else:
                lostmoney = True
                Player.gold -= casinogold
                Player.activities.append(f"Lost {casinogold} golds from casino")
        else:
            lostmoney = False
            Player.gold += casinogold
            Player.activities.append(f"Won {casinogold} golds from casino")

    return render_template("index.html", gold=Player.gold, activities=Player.activities, lostmoney=lostmoney)

if __name__ == "__main__":
    app.run(debug=True)