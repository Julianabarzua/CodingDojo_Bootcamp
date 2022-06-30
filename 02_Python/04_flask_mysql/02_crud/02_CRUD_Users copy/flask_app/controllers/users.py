from flask import render_template, request, redirect
# importar la clase de friend.py

from flask_app import app
# ...server.py

from flask_app.models.users import User


@app.route("/")
def mainroute():
    return redirect("/users")

@app.route("/users")
def index():
    # llamar al método de clase get all para obtener todos los amigos
    users = User.get_all()
    print(users)
    return render_template("index.html", users = users)
            

@app.route("/users/<id>")
def show(id):
    # llamar al método de clase get all para obtener todos los amigos
    user = User.get_one(id=id)
    print(user)
    return render_template("show.html", user = user)

@app.route("/users/<id>/destroy")
def delete(id):
    # llamar al método de clase get all para obtener todos los amigos
    User.delete(id=id)
    return redirect("/")

@app.route("/users/<id>/edit")
def edit(id):
    user = User.get_one(id=id)
    return render_template("edit.html",user=user)

@app.route("/users/new")
def new():

    return render_template("new_user.html")

# fragmento de código relevante de server.py
@app.route('/create_user', methods=["POST"])
def create_friend():
    # Primero hacemos un diccionario de datos a partir de nuestro request.form proveniente de nuestra plantilla
    # Las claves en los datos tienen que alinearse exactamente con las variables en nuestra cadena de consulta
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    # Pasamos el diccionario de datos al método save de la clase Friend
    User.save(data)
    # No olvides redirigir después de guardar en la base de datos
    return redirect('/users')

@app.route('/edit_user/<id>', methods=["POST"])
def edit_fuser(id):
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"],
    }
    User.update(data, id=id)
    return redirect('/users')