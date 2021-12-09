from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.user import User


@app.route('/user')
def index():
    users = User.get_all()
    print(users)
    return render_template("read.html", all_users=users)


@app.route('/user/new')
def usernew():
    pass
    return render_template("create.html")


@app.route('/user/new/create', methods=["POST"])
def create_user():

    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "em": request.form["em"]
    }
    User.save(data)
    return redirect('/user')


@app.route('/user/show/<int:id>')
def show_user(id):
    data = {
        "id": id,
    }
    info = User.show(data)
    return render_template('show.html', id=id, info=info)


@app.route('/user/edit/<int:id>')
def edit_user_page(id):
    data = {
        "id": id,
    }
    info = User.show(data)
    return render_template('edit.html', id=id, info=info)


@app.route('/user/edit/<int:id>/update', methods=["POST"])
def edit_user(id):
    data = {
        "id": id,
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "em": request.form["em"]
    }
    User.edit(data)
    return redirect('/user')


@app.route('/user/delete/<int:id>')
def delete_user_page(id):
    pass
    return render_template('delete.html', id=id)


@app.route('/user/delete/<int:id>/confirm', methods=["POST"])
def delete_user(id):
    data = {
        "id": id,
    }
    User.delete(data)
    return redirect('/user')
