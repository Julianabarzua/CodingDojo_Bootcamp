from flask import Flask, render_template, request, redirect, session
import random



app = Flask(__name__)
app.secret_key = "Calamardo"



@app.route('/')
def index():
    number = random.randint(1,100)
    session['number'] = number
    session['tries'] = 0

    return render_template("index.html")

@app.route('/test', methods=['POST'])
def test():
    session['tries'] +=1
    
    if int(request.form['guess']) == session['number']:
        return redirect('/win')
    elif int(request.form['guess']) < session['number']:
        if session['tries'] >= 5:
            return redirect('/lose')
        return redirect('/toolow')
    else :
        if session['tries'] >= 5:
            return redirect('/lose')
        return redirect('/toohigh')

@app.route('/toolow')
def too_low():

    return render_template("toolow.html", tries = session['tries'])

@app.route('/toohigh')
def too_high():

    return render_template("toohigh.html", tries = session['tries'])

@app.route('/win')
def win():
    return render_template("win.html", number =session['number'],  tries = session['tries'] )

@app.route('/reset')
def reset():

    return redirect("/")

@app.route('/lose')
def lose():

    return render_template("lose.html", number =session['number'],  tries = session['tries'] )






if __name__ == "__main__":
    app.run(debug=True)

