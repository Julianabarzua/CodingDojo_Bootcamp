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