from flask import Flask, render_template, request, redirect
# importar la clase de friend.py
from users import User
app = Flask(__name__)

@app.route("/users")
def index():
    # llamar al método de clase get all para obtener todos los amigos
    users = User.get_all()
    print(users)
    return render_template("index.html", users = users)
            

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


if __name__ == "__main__":
    app.run(debug=True)