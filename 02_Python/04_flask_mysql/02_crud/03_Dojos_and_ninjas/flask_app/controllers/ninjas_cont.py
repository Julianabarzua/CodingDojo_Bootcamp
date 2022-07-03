from flask import render_template, request, redirect
# importar la clase de friend.py

from flask_app import app
# ...server.py

from flask_app.models.ninjas_model import Ninja
from flask_app.models.dojos_model import Dojo


@app.route("/")
def mainroute():
    return redirect("/dojos")

@app.route("/dojos")
def index():
    # llamar al método de clase get all para obtener todos los amigos
    dojos = Dojo.get_all()
    print(dojos)
    return render_template("index.html", dojos=dojos)

@app.route("/create_dojo",  methods=["POST"])
def create_dojo():
    data = {
        "name": request.form["name"]
    }
    Dojo.save(data)
    return redirect("/dojos")

@app.route("/dojos/<id>")
def show_dojo(id):

    data = {
        "id": id
    }
    dojo = Dojo.get_dojo_with_ninjas(data)

    return render_template("show.html", dojo=dojo)

@app.route("/ninjas")
def new_ninja():
    dojos = Dojo.get_all()
    print(dojos)
    return render_template('new_ninja.html', dojos=dojos)


@app.route("/create_ninja",  methods=["POST"])
def create_ninja():
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "age" : request.form["age"],
        "dojo_id" : request.form["dojo"]
    }

    Ninja.save(data)
    id=request.form["dojo"]
    return redirect("/dojos/"+id)
