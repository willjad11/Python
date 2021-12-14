from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
import datetime

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASS_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')

@staticmethod
def time_since(delta):
    if (datetime.datetime.now() - delta).days == 0:
        if (datetime.datetime.now() - delta).seconds//3600 == 0:
            if ((datetime.datetime.now() - delta).seconds//60) % 60 == 0:
                return 'sent {} seconds ago'.format(
                    int((datetime.datetime.now() - delta).total_seconds() % 60))
            return 'sent {} minutes, {} seconds ago'.format(
                ((datetime.datetime.now() - delta).seconds//60) % 60,
                int((datetime.datetime.now() - delta).total_seconds() % 60))
        return 'sent {} hours, {} minutes, {} seconds ago'.format(
            (datetime.datetime.now() - delta).seconds//3600,
            ((datetime.datetime.now() - delta).seconds//60) % 60,
            int((datetime.datetime.now() - delta).total_seconds() % 60))
    else:
        return 'sent {} days, {} hours, {} minutes, {} seconds passed.'.format(
            (datetime.datetime.now() - delta).days,
            (datetime.datetime.now() - delta).seconds//3600,
            (((datetime.datetime.now() - delta).seconds//60) % 60,
                int(((datetime.datetime.now() - delta).total_seconds() % 60))))

class Message:

    def __init__(self, data):

        self.id = data['message_id']
        self.sender_id = data['sender_id']
        self.sender_first_name = data['sender_first_name']
        self.sender_last_name = data['sender_last_name']
        self.recipient_id = data['recipient_id']
        self.recipient_first_name = data['recipient_first_name']
        self.recipient_last_name = data['recipient_last_name']
        self.message = data['message']
        self.created_at = data['created_at']
        self.since_created = time_since(data['created_at'])
        self.updated_at = data['updated_at']
        self.since_updated = time_since(data['updated_at'])


    @staticmethod
    def send_message(data):
        query = '''
        INSERT INTO messages(sender_id , recipient_id , message , created_at , updated_at) 
        VALUES(%(sid)s , %(rid)s , %(msg)s , NOW(), NOW());
        '''
        return connectToMySQL("wall").query_db(query, data)


    def verify_message(data):
        verified = False
        query = '''
        SELECT users.id, messages.id
        FROM users JOIN messages ON messages.sender_id = users.id 
        JOIN users AS recipients ON messages.recipient_id = recipients.id 
        WHERE recipients.id = %(rid)s AND messages.id = %(mid)s;
        '''
        results = connectToMySQL("wall").query_db(query, data)
        print(results)
        if results:
            verified = True
        return verified


    @staticmethod
    def delete_message(data):
        query = '''
        DELETE FROM messages
        WHERE messages.id = %(mid)s AND messages.recipient_id = %(rid)s;
        '''
        return connectToMySQL("wall").query_db(query, data)

    @staticmethod
    def message_count(data):
        query = '''
        SELECT COUNT(messages.id) AS count
    FROM users JOIN messages ON messages.sender_id = users.id 
    JOIN users AS recipients ON messages.recipient_id = recipients.id 
    WHERE users.id = %(id)s;
        '''
        return connectToMySQL("wall").query_db(query, data)


    @classmethod
    def get_all_messages(cls, data):
        query = '''
                SELECT users.id, users.first_name AS sender_first_name, users.last_name AS sender_last_name, messages.id AS message_id, messages.message, messages.created_at, 
                messages.updated_at, messages.sender_id, messages.recipient_id, recipients.first_name AS recipient_first_name, recipients.last_name  AS recipient_last_name
                FROM users JOIN messages ON messages.sender_id = users.id 
                JOIN users AS recipients ON messages.recipient_id = recipients.id 
                WHERE recipients.id = %(id)s;
                '''
        results = connectToMySQL("wall").query_db(query, data)
        messages = []
        if results:
            for message in results:
                messages.append(cls(message))
            return messages
        else:
            print("No results")