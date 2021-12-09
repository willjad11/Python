from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/ninja')
def ninja_index():
    ninjas = Ninja.get_all()
    dojos = Dojo.get_all()
    return render_template("read_ninjas.html", all_ninjas=ninjas, all_dojos=dojos)


@app.route('/ninja/new')
def ninja_new():
    dojos = Dojo.get_all()
    return render_template("create_ninja.html", all_dojos=dojos)


@app.route('/ninja/new/create', methods=["POST"])
def create_ninja():

    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "age": request.form["age"],
        "did": request.form["did"]
    }
    Ninja.save(data)
    return redirect('/ninja')


@app.route('/ninja/show/<int:id>')
def show_ninja(id):
    ninjadata = {
        "id": id,
    }
    ninja = Ninja.show(ninjadata)
    dojodata = {
        "id": ninja[0]['dojo_id'],
    }
    dojo = Dojo.show(dojodata)
    return render_template('show_ninja.html', id=id, ninja=ninja, dojo=dojo)


@app.route('/ninja/edit/<int:id>')
def edit_ninja_page(id):
    ninjadata = {
        "id": id,
    }
    ninja = Ninja.show(ninjadata)
    dojos = Dojo.get_all()
    return render_template('edit_ninja.html', id=id, ninja=ninja, dojos=dojos)


@app.route('/ninja/edit/<int:id>/update', methods=["POST"])
def edit_ninja(id):
    data = {
        "id": id,
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "age": request.form["age"],
        "did": request.form["did"],
    }
    Ninja.edit(data)
    return redirect('/ninja')


@app.route('/ninja/delete/<int:id>')
def delete_ninja_page(id):
    pass
    return render_template('delete_ninja.html', id=id)


@app.route('/user/delete/<int:id>/confirm', methods=["POST"])
def delete_ninja(id):
    data = {
        "id": id,
    }
    Ninja.delete(data)
    return redirect('/ninja')
