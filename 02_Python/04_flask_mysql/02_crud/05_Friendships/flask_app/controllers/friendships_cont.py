from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.friendships_mod import User

@app.route("/")
def mainroute():
    friendships = User.get_all_friendships()
    users = User.get_all()

    return render_template("index.html", friendships=friendships, users = users)

@app.route("/add_user", methods=['POST'])
def add_user():
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"]
    }
    User.save(data)
    return redirect("/")


@app.route("/add_friendship", methods=['POST'])
def add_friendship():
    if request.form["user"] == request.form["friend"]:
        return redirect("/")
    data = {
        "userid": request.form["user"],
        "friendid": request.form["friend"]
    }
    User.add_friendship(data)
    return redirect("/")