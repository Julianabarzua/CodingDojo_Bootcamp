from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', rows=8, columns=8, color1='white', color2='black')

@app.route('/<int:rows>')
def index2(rows):
    return render_template('index.html', rows=rows, columns=8, color1='white', color2='black')

@app.route('/<int:rows>/<int:columns>')
def index3(rows, columns):
    return render_template('index.html', rows=rows, columns=columns, color1='white', color2='black')

@app.route('/<int:rows>/<int:columns>/<color1>/<color2>')
def index4(rows, columns, color1, color2):
    return render_template('index.html', rows=rows, columns=columns, color1=color1, color2=color2)


if __name__ == "__main__" :
    app.run()