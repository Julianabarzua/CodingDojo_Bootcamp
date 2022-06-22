
from flask import Flask  # Importa Flask para permitirnos crear nuestra aplicación

app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"

@app.route('/')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def hola_mundo():
    return 'Hola Mundo!'  # Devuelve la cadena '¡Hola Mundo!' como respuesta


    
@app.route('/success')
def success():
    return "success"

@app.route('/hola/<nombre>')
def hola(nombre):
    return f"Hola, " + nombre

@app.route('/users/<username>/<id>')
def show_user_profile(username,id):
    return "<h1 style='color:red;'>Username</h1>" + username + ", ID: " + id



if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente    
    app.run(debug=True)    # Ejecuta la aplicación en modo de depuración

