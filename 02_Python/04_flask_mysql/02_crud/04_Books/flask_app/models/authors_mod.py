from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import books_mod

class Author:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
        self.favorites = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors;"
        results = connectToMySQL('books_schema').query_db(query)
        authors = []
        for author in results:
            authors.append( cls(author) )
        return authors

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO authors ( name , created_at, updated_at ) VALUES ( %(name)s , NOW() , NOW() );"
        return connectToMySQL('books_schema').query_db( query, data )

    @classmethod
    def get_author_with_books(cls,data):
        query = "SELECT * FROM authors LEFT JOIN favorites ON favorites.author_id = authors.id LEFT JOIN books ON favorites.book_id = books.id WHERE authors.id = %(id)s;"
        results = connectToMySQL('books_schema').query_db(query, data)
        author = cls(results[0])
        for row in results:
            book_data = {
                "id" : row['books.id'],
                "title" : row['title'],
                "page_num" : row['page_num'],
                "created_at" : row['books.created_at'],
                "updated_at" : row['books.updated_at']
            }
            author.favorites.append(books_mod.Book(book_data))

        return author

    @classmethod
    def add_favorite(cls,data):
        query = "INSERT INTO favorites (author_id,book_id) VALUES (%(author_id)s,%(book_id)s);"
        return connectToMySQL('books_schema').query_db(query,data);

