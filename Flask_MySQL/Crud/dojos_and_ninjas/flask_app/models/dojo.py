from flask_app.config.mysqlconnection import connectToMySQL



class Dojo:

    def __init__(self, data):

        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"

        results = connectToMySQL('dojoninja').query_db(query)

        dojos = []

        if results:
            for dojo in results:
                dojos.append(cls(dojo))
            return dojos
        else:
            print("No results")

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos ( name, created_at, updated_at ) VALUES ( %(name)s , NOW() , NOW() );"
        return connectToMySQL('dojoninja').query_db(query, data)

    @classmethod
    def edit(cls, data):
        query = "UPDATE dojos SET name = %(name)s , updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL('dojoninja').query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "UPDATE ninjas SET dojo_id = 6 WHERE dojo_id = %(id)s;"
        connectToMySQL('dojoninja').query_db(query, data)
        query = "DELETE FROM dojos WHERE id = %(id)s;"
        return connectToMySQL('dojoninja').query_db(query, data)

    @classmethod
    def show(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        return connectToMySQL('dojoninja').query_db(query, data)
