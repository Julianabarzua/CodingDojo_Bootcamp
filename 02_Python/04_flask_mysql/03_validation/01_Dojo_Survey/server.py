from flask import Flask, render_template, request, redirect, session
from flask_app import app
from flask_app.models.table_1 import Table_1


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/process', methods=['POST'])
def create_user():
    data = {
        "name": request.form["name"],
        "location" : request.form["location"],
        "language" : request.form["language"],
        "comment" : request.form["text"]
    }

    if not Table_1.validate_info(data):
        return redirect ("/")
    Table_1.save(data)
    return redirect('/result')

@app.route('/result')
def show_result():
    return "Succesfully added"

if __name__ == "__main__":
    app.run(debug=True)

