from flask import Flask, render_template, request, redirect, session
import random
import datetime



app = Flask(__name__)
app.secret_key = "Calamardo"


@app.route('/')
def index():
    if 'gold' in session:
        session['gold'] = session['gold']
    else:
        session['gold'] = 0

    if 'activities' in session:
        session['activities'] = session['activities']
    else:
        session['activities'] = []

    return render_template("index.html", gold=session['gold'], message=session['activities'])


@app.route('/process_money', methods=['POST'])
def processmoney():
    if request.form['building'] == 'farm':
        dif= random.randint(10,20)
        session['gold'] += dif
        message ='<h4 style="color:green;">Earned '+str(dif)+' golds from the farm! '+datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")+'</h4>'
        session['activities'].insert(0,message)
    elif request.form['building'] == 'cave':
        dif= random.randint(5,10)
        session['gold'] += dif
        message ='<h4 style="color:green;">Earned '+str(dif)+' golds from the cave! '+datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")+'</h4>'
        session['activities'].insert(0,message)
    elif request.form['building'] == 'house':
        dif= random.randint(2,5)
        session['gold'] += dif
        message ='<h4 style="color:green;">Earned '+str(dif)+' golds from the house! '+datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")+'</h4>'
        session['activities'].insert(0,message)
    elif request.form['building'] == 'casino':
        dif= random.randint(-50,50)
        session['gold'] += dif
        if dif > 0:
            message ='<h4 style="color:green;">Earned '+str(dif)+' golds from the casino! '+datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")+'</h4>'
            session['activities'].insert(0,message)

        else:
            message ='<h4 style="color:red;">Lost '+str(abs(dif))+' golds from the casino! '+datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")+'</h4>'
            session['activities'].insert(0,message)
    return redirect("/")




@app.route('/reset', methods=['POST'])
def reset():
    session['activities'] = []
    session['gold'] = 0
    return redirect('/')




if __name__ == "__main__":
    app.run(debug=True)
