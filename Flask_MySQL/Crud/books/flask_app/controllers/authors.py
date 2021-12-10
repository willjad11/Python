from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.author import Author
from flask_app.models.book import Book


@app.route('/authors')
def author_index():
    authors = Author.get_all()
    return render_template("authors.html", all_authors=authors)


@app.route('/authors/<int:id>')
def author_fav_index(id):
    data = {
        "id": id
    }
    author = Author.show(data)
    favs = Author.favorites(data)
    notfavs = Author.not_favorites(data)
    return render_template("author_fav.html", id=id, author=author, favs=favs, notfavs=notfavs)


@app.route('/authors/<int:id>/add', methods=["POST"])
def author_add_fav(id):
    data = {
        "authorid": request.form['authorid'],
        "id": request.form['id']
    }
    Author.add_favorites(data)
    return redirect(f"/authors/{id}")

@app.route('/authors/create', methods=["POST"])
def create_author():
    data = {
        "name": request.form["name"]
    }
    Author.save(data)
    return redirect('/authors')
