from flask_app.config.mysqlconnection import connectToMySQL



class Book:

    def __init__(self, data):

        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"

        results = connectToMySQL('books').query_db(query)

        dojos = []

        if results:
            for dojo in results:
                dojos.append(cls(dojo))
            return dojos
        else:
            print("No results")

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"

        results = connectToMySQL('books').query_db(query)

        books = []

        if results:
            for book in results:
                books.append(cls(book))
            return books
        else:
            print("No results")

    @classmethod
    def save(cls, data):
        query = "INSERT INTO books ( title, num_of_pages, created_at, updated_at ) VALUES ( %(title)s , %(pages)s , NOW() , NOW() );"
        return connectToMySQL('books').query_db(query, data)

    @classmethod
    def show(cls, data):
        query = "SELECT * FROM books WHERE id = %(id)s;"
        return connectToMySQL('books').query_db(query, data)

    @classmethod
    def favorites(cls, data):
        query = "SELECT authors.id, authors.name FROM books JOIN favorites ON favorites.books_id = books.id JOIN authors ON favorites.authors_id = authors.id WHERE books.id = %(id)s;"
        return connectToMySQL('books').query_db(query, data)

    @classmethod
    def not_favorites(cls, data):
        favs = Book.favorites(data)
        query = "SELECT authors.id, authors.name, books.title FROM books JOIN favorites ON favorites.books_id = books.id JOIN authors ON authors.id = favorites.authors_id WHERE %(id)s NOT IN(books.id)"
        for i in range(len(favs)):
            query += " AND authors.id != " + str(favs[i]['id'])
        query += " GROUP BY authors.name;"
        return connectToMySQL('books').query_db(query, data)

    @classmethod
    def add_favorites(cls, data):
        query = "INSERT INTO favorites(authors_id, books_id) VALUE(%(authorid)s, %(id)s);"
        print(query)
        return connectToMySQL('books').query_db(query, data)
