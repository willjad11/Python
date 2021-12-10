from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Email:

    def __init__(self, data):

        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM email;"
        results = connectToMySQL('emails').query_db(query)
        emails = []
        if results:
            for email in results:
                emails.append(cls(email))
            return emails
        else:
            print("No results")

    @classmethod
    def save(cls, data):
        query = "INSERT INTO email ( email, created_at, updated_at ) VALUES ( %(email)s , NOW() , NOW() );"
        return connectToMySQL('emails').query_db(query, data)
    
    @staticmethod
    def validate_email(email):
        is_valid = True
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(email['email']):
            flash("Invalid email address!")
            is_valid = False
        return is_valid
    
    @staticmethod
    def is_duplicate(data):
        is_dup = False
        query = "SELECT * FROM email where email = %(email)s;"
        results = connectToMySQL('emails').query_db(query, data)
        if results:
            if results[0]['email'] == data['email']:
                flash("Duplicate email address.")
                is_dup = True
        return is_dup
