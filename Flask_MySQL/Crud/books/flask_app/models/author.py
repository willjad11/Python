from flask_app.config.mysqlconnection import connectToMySQL



class Author:

    def __init__(self, data):

        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors;"

        results = connectToMySQL('books').query_db(query)

        authors = []

        if results:
            for author in results:
                authors.append(cls(author))
            return authors
        else:
            print("No results")

    @classmethod
    def save(cls, data):
        query = "INSERT INTO authors ( name, created_at, updated_at ) VALUES ( %(name)s , NOW() , NOW() );"
        return connectToMySQL('books').query_db(query, data)

    @classmethod
    def show(cls, data):
        query = "SELECT * FROM authors WHERE id = %(id)s;"
        return connectToMySQL('books').query_db(query, data)

    @classmethod
    def favorites(cls, data):
        query = "SELECT books.id, books.title, books.num_of_pages FROM authors JOIN favorites ON favorites.authors_id = authors.id JOIN books ON favorites.books_id = books.id WHERE authors.id = %(id)s;"
        return connectToMySQL('books').query_db(query, data)

    @classmethod
    def not_favorites(cls, data):
        favs = Author.favorites(data)
        query = "SELECT books.id, authors.name, books.title FROM authors JOIN favorites ON favorites.authors_id = authors.id JOIN books ON books.id = favorites.books_id WHERE %(id)s NOT IN(authors.id)"
        for i in range(len(favs)):
            query += " AND books.id != " + str(favs[i]['id'])
        query += " GROUP BY books.title;"
        return connectToMySQL('books').query_db(query, data)

    @classmethod
    def add_favorites(cls, data):
            query = "INSERT INTO favorites(authors_id, books_id) VALUE(%(authorid)s, %(id)s);"
            return connectToMySQL('books').query_db(query, data)
