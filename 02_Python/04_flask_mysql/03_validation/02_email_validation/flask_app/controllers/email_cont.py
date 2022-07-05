from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.email_model import Email

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add_email", methods =["POST"] )
def create_email():
    if not Email.validate_email(request.form):
        return redirect ("/")

    
    data = {
        "email" : request.form["email"]
    }
    Email.save(data)
    return redirect("/success")


@app.route("/success")
def success():
    emails=Email.get_all()
    return render_template("list.html", emails=emails)

@app.route("/delete/<id>")
def delete(id):
    Email.delete(id)
    return redirect("/success")