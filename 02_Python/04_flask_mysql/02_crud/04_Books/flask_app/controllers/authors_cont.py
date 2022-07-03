from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.authors_mod import Author
from flask_app.models.books_mod import Book

@app.route("/")
def mainroute():
    return redirect("/authors")

@app.route("/authors")
def index():
    authors = Author.get_all()
    return render_template("index.html", authors=authors)

@app.route("/create_author",  methods=["POST"])
def create_author():
    data = {
        "name": request.form["name"]
    }
    Author.save(data)
    return redirect("/authors")

@app.route("/authors/<id>")
def show_authors(id):

    data = {
        "id": id
    }
    author = Author.get_author_with_books(data)
    books = Book.get_all()
    return render_template("show.html", author=author, books=books)

@app.route("/add_favorite/<author_id>", methods=["POST"] )
def add_favorite(author_id):
    data = {
        'author_id' : author_id,
        'book_id' : request.form['book']
    }

    Author.add_favorite(data)
    return redirect("/authors/"+author_id)