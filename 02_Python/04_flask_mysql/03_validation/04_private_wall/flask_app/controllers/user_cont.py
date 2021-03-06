from operator import methodcaller
from flask import flash, render_template, request, redirect, session
from flask_app import app
from flask_app.models.user_model import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route("/")
def index():
    if 'user_id' in session:
        return redirect('/success')
    return render_template("index.html")

@app.route("/add_user", methods=['POST'])
def add_user():
    
    if not User.validate_user(request.form):
        return redirect("/")
    
    pw_hash = bcrypt.generate_password_hash(request.form['password'])

    data = {
        "firstname" : request.form["fname"],
        "lastname" : request.form["lname"],
        "email" : request.form["email"],
        "password" : pw_hash
    }
    user_id = User.save(data)
    session['user_id'] = user_id
    print(session['user_id'])
    return redirect("/success")

@app.route("/success")
def logedin():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id":session['user_id']
    }
    otherusers = User.allusersbutloged(data)
    usuarioLogeado = User.logedUser(data)
    messages = User.messagesforuser(data)
    print(messages)
    count_from = User.count_from_messages(data)
    count_to = User.count_to_messages(data)
    return render_template("success.html", usuarioLogeado = usuarioLogeado, otherusers = otherusers, messages=messages, count_from = count_from[0]['COUNT(id)'], count_to = count_to[0]['COUNT(id)'])

@app.route('/login', methods=['POST'])
def login():
    data = {
        "email": request.form['email']
    }
    usuario = User.getEmail(data)
    print(usuario, "EL USUARIO EXISTE?")
    if not usuario:
        flash("User not registered")
        return redirect('/')
    
    if not bcrypt.check_password_hash(usuario[0]['password'], request.form['password']):
        flash("Invalid Email/Password")
        return redirect('/')

    session['user_id'] = usuario[0]['id']
    return redirect('/success')

@app.route("/logout", methods=['GET'])
def logout():
    session.clear()
    return redirect('/')

@app.route("/add_message/<to_id>", methods = ['POST'])
def add_message(to_id):
    
    if not User.validate_message(request.form):
        return redirect("/success")
    
    data = {
        "to_id": to_id,
        "from_id": request.form['from_id'],
        "content": request.form['content']
    }
    User.save_message(data)

    return redirect("/success")

@app.route("/delete_message/<id>")
def delete_message(id):
    data = {
        "id": id
    }    
    User.delete_message(data)
    return redirect("/success")
