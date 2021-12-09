from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo


@app.route('/dojo')
def dojo_index():
    ninjas = Ninja.get_all()
    dojos = Dojo.get_all()
    return render_template("read_dojos.html", all_ninjas=ninjas, all_dojos=dojos)


@app.route('/dojo/new')
def dojo_new():
    dojos = Dojo.get_all()
    return render_template("create_dojo.html", all_dojos=dojos)


@app.route('/dojo/new/create', methods=["POST"])
def create_dojo():
    data = {
        "name": request.form["name"],
    }
    Dojo.save(data)
    return redirect('/dojo')


@app.route('/dojo/show/<int:id>')
def show_dojo(id):
    ninjas = Ninja.get_all()
    dojodata = {
        "id": id
    }
    dojo = Dojo.show(dojodata)
    return render_template('show_dojo.html', id=id, dojo=dojo, ninjas=ninjas)


@app.route('/dojo/edit/<int:id>')
def edit_dojo_page(id):
    dojodata = {
        "id": id,
    }
    dojo = Dojo.show(dojodata)
    return render_template('edit_dojo.html', id=id, dojo=dojo)


@app.route('/dojo/edit/<int:id>/update', methods=["POST"])
def edit_dojo(id):
    data = {
        "id": id,
        "name": request.form["name"],
    }
    Dojo.edit(data)
    return redirect('/dojo')


@app.route('/dojo/delete/<int:id>')
def delete_dojo_page(id):
    pass
    return render_template('delete_dojo.html', id=id)


@app.route('/dojo/delete/<int:id>/confirm', methods=["POST"])
def delete_dojo(id):
    data = {
        "id": id,
    }
    Dojo.delete(data)
    return redirect('/dojo')
