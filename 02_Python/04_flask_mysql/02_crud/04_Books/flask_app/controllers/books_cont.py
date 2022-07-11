from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.authors_mod import Author
from flask_app.models.books_mod import Book

@app.route("/books")
def show_books():
    books = Book.get_all()
    return render_template('books.html', books = books)

@app.route("/create_book",  methods=["POST"])
def create_book():
    data = {
        "title": request.form["title"],
        "page_num": request.form["page_num"]
    }
    Book.save(data)
    return redirect("/books")

@app.route("/books/<id>")
def show_book(id):
    data = {
        "id": id
    }
    book = Book.get_book_with_authors(data)
    authors = Author.unfavorited_authors(data)
    return render_template("show_book.html", book=book, authors=authors)

@app.route("/add_favorited_by/<book_id>", methods=["POST"] )
def add_favorited_by(book_id):
    data = {
        'author_id' : request.form['author'],
        'book_id' : book_id
    }

    Author.add_favorite(data)
    return redirect("/books/"+book_id)