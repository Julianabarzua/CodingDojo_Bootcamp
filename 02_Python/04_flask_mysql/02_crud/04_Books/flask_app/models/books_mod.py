from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import authors_mod 

class Book:
    def __init__(self,data):
        self.id = data['id']
        self.title = data['title']
        self.page_num = data['page_num']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.favorited_by = []
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL('books_schema').query_db(query)
        books = []
        for book in results:
            books.append( cls(book) )
        return books

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO books ( title , page_num, created_at, updated_at ) VALUES ( %(title)s , %(page_num)s, NOW() , NOW() );"
        return connectToMySQL('books_schema').query_db( query, data )

    @classmethod
    def get_book_with_authors(cls,data):
        query = """
                    SELECT * 
                    FROM books 
                    LEFT JOIN favorites ON favorites.book_id = books.id 
                    LEFT JOIN authors ON favorites.Author_id = authors.id 
                    WHERE books.id =%(id)s ;
                """
        results = connectToMySQL('books_schema').query_db(query, data)
        book = cls(results[0])
        for row in results:
            author_data = {
                "id" : row['authors.id'],
                "name" : row['name'],
                "created_at" : row['authors.created_at'],
                "updated_at" : row['authors.updated_at']
            }
            book.favorited_by.append(authors_mod.Author(author_data))

        return book

