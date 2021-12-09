from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:

    def __init__(self, data):

        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL('dojoninja').query_db(query)
        ninjas = []
        if results:
            for ninja in results:
                ninjas.append(cls(ninja))
            return ninjas
        else:
            print("No results")

    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas ( first_name, last_name, age, dojo_id, created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(age)s , %(did)s , NOW() , NOW() );"
        return connectToMySQL('dojoninja').query_db(query, data)

    @classmethod
    def edit(cls, data):
        query = "UPDATE ninjas SET first_name = %(fname)s, last_name = %(lname)s, age = %(age)s, dojo_id = %(did)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL('dojoninja').query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM ninjas WHERE id = %(id)s;"
        return connectToMySQL('dojoninja').query_db(query, data)

    @classmethod
    def show(cls, data):
        query = "SELECT * FROM ninjas WHERE id = %(id)s;"
        return connectToMySQL('dojoninja').query_db(query, data)
