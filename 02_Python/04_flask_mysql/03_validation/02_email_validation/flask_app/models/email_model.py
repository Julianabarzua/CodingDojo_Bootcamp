from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Email:
    def __init__(self,data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails;"
        results = connectToMySQL('email_schema').query_db(query)
        emails = []
        for email in results:
            emails.append( cls(email) )
        return emails

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO emails (email , created_at, updated_at ) VALUES (%(email)s , NOW() , NOW() );"
        return connectToMySQL('email_schema').query_db( query, data )

    @classmethod
    def delete(cls, id):
        query = "DELETE FROM emails WHERE id ="+id
        return connectToMySQL('email_schema').query_db( query)

    @staticmethod
    def validate_email(email):
        
        all_emails = Email.get_all()
        is_valid = True

        if not EMAIL_REGEX.match(email['email']):
            flash("Invalid email address!")
            is_valid = False

        for correo in all_emails:
            if email['email'] == correo.email:
                flash('Mail already registered, please add a new one')
                is_valid = False

        return is_valid