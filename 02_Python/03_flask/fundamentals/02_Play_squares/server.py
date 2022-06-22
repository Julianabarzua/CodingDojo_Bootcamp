from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')
def index():
    return render_template('index.html', times=3, color='#A2C3E8')


@app.route('/play/<int:num>')
def squares2(num):
    return render_template('index.html', times=num, color='#A2C3E8')

@app.route('/play/<int:num>/<string:color>')
def squares3(num,color):
    return render_template('index.html', times=num, color=color)

if __name__ == "__main__" :
    app.run()