from flask import Flask, render_template, request, redirect, session



app = Flask(__name__)
app.secret_key = "Calamardo"



@app.route('/')
def index():

    if 'counter1' in session:
        session['counter1'] += 1
        session['counter2'] += 1
    else:
        session['counter1'] = 1
        session['counter2'] = 1

    return render_template("index.html", counter1 = session['counter1'], counter2 = session['counter2'])

@app.route('/destroy_session',  methods=['POST'])
def reset():
    session['counter1'] = 0
    session['counter2'] = 0
    return redirect("/")

@app.route('/mas_dos',  methods=['POST'])
def mas_dos():
    session['counter1'] += 1
    return redirect("/")

@app.route('/contador',  methods=['POST'])
def contador():

    session['counter1'] = session['counter1'] + int(request.form['contador']) - 1
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)

