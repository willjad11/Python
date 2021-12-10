from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.book import Book
from flask_app.models.author import Author


@app.route('/books')
def book_index():
    books = Book.get_all()
    return render_template("books.html", all_books=books)


@app.route('/books/<int:id>')
def book_fav_index(id):
    data = {
        "id": id
    }
    book = Book.show(data)
    favs = Book.favorites(data)
    notfavs = Book.not_favorites(data)
    return render_template("book_fav.html", id=id, book=book, favs=favs, notfavs=notfavs)


@app.route('/books/<int:id>/add', methods=["POST"])
def book_add_fav(id):
    data = {
        "id": request.form['id'],
        "authorid": request.form['authorid']
    }
    Book.add_favorites(data)
    return redirect(f"/books/{id}")


@app.route('/books/create', methods=["POST"])
def create_book():
    data = {
        "title": request.form["title"],
        "pages": request.form["pages"]
    }
    Book.save(data)
    return redirect('/books')
