from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Table_1:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.languague = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO table1 ( name , location , language , comment, created_at, updated_at ) VALUES ( %(name)s , %(location)s , %(language)s, %(comment)s, NOW() , NOW() );"
        return connectToMySQL('dojo_survey_schema').query_db( query, data )

    @staticmethod
    def validate_info(table_1):
        is_valid = True
        if len(table_1['name']) < 1:
            flash("You have to fill out your name")
            is_valid = False

        
        return is_valid