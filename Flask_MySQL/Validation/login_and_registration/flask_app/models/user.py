from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:

    def __init__(self, data):

        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def register(cls, data):
        query = "INSERT INTO users ( first_name, last_name, email, password, created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(em)s , %(pas)s , NOW() , NOW() );"
        return connectToMySQL('register').query_db(query, data)

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(em)s;"
        result = connectToMySQL("register").query_db(query, data)
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL("register").query_db(query, data)
        # Didn't find a matching user
        if not result:
            return False
        return cls(result[0])
    
    @staticmethod
    def validate_email(email):
        is_valid = True
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(email['em']):
            is_valid = False
        return is_valid
