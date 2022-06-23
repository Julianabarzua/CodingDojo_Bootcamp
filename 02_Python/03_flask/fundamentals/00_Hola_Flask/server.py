
from flask import Flask, render_template  # Importa Flask para permitirnos crear nuestra aplicación

app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"

@app.route('/')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def index():
    return render_template('index.html', frase='Hola', times=5)


    
@app.route('/success')
def success():
    return "success"

@app.route('/hola/<nombre>')
def hola(nombre):
    return f"Hola, " + nombre

@app.route('/users/<username>/<id>')
def show_user_profile(username,id):
    return "<h1 style='color:red;'>Username</h1>" + username + ", ID: " + id


@app.route('/lists')
def render_lists():
    # Muy pronto, obtendremos datos de una base de datos, pero por ahora, estamos codificando datos
    estudiantes_info = [
        {'name' : 'Michael', 'edad' : 35},
        {'name' : 'John', 'edad' : 30 },
        {'name' : 'Mark', 'edad' : 30},
        {'name' : 'KB', 'edad' : 27}
    ]
    return render_template("lists.html", random_numbers = [3,1,5], estudiantes = estudiantes_info)





if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente    
    app.run(debug=True)    # Ejecuta la aplicación en modo de depuración

