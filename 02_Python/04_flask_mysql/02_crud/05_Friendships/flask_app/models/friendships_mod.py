from ast import Return
from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users ( first_name , last_name, created_at, updated_at ) VALUES ( %(fname)s ,%(lname)s, NOW() , NOW() );"
        return connectToMySQL('friendship_schema').query_db( query, data )

    @classmethod
    def get_all(cls):
        query = "SELECT id, concat(first_name,' ', last_name) as name FROM users;"
        users = connectToMySQL('friendship_schema').query_db(query)
        return users

    @classmethod
    def add_friendship(cls, data):
        query = "INSERT INTO friendships ( User_id , friend_id, created_at, updated_at ) VALUES ( %(userid)s ,%(friendid)s, NOW() , NOW() );"
        return connectToMySQL('friendship_schema').query_db( query, data )

    @classmethod
    def get_all_friendships(cls):
        query="""
                    SELECT concat(u.first_name, " ", u.last_name) as User, concat(u2.first_name," ", u2.last_name) as Friend
                    FROM users as u
                    LEFT JOIN friendships as f ON u.id = f.user_id
                    JOIN users as u2 ON f.friend_id = u2.id
                    ORDER BY User;
                    """
        return connectToMySQL('friendship_schema').query_db(query)

