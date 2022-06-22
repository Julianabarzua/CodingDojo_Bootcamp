from flask import Flask

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return 'Hola Mundo!'


@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<string:name>')
def say_name(name):
    return 'Hola, '+ name + '!'

@app.route('/repeat/<int:num>/<string:word>')
def repeat_word(num,word):
    return (word + "<br>") * num

@app.route('/<generic>')
def error(generic):
    return "Sorry, your mistake"


if __name__ == "__main__" :
    app.run()
