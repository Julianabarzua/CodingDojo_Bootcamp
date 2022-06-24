from itertools import count
from flask import Flask, render_template, request, redirect
from datetime import datetime


app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    date = datetime.now().strftime('%b %e, %Y at %H:%M:%S')
    count=int(request.form['strawberry'])+int(request.form['raspberry'])+int(request.form['apple'])
    return render_template("checkout.html", counter=count, date=date)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)