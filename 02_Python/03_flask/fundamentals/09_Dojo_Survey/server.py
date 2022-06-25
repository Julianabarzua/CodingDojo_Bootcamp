from flask import Flask, render_template, request, redirect, session



app = Flask(__name__)
app.secret_key = "Calamardo"


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/process', methods=['POST'])
def create_user():
    print(request.form)
    session['name']=request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['text'] = request.form['text']

    return redirect('/result')

@app.route('/result')
def show_result():
    return render_template('show.html', name=session['name'],loc=session['location'],lan =  session['language'], txt=session['text']  )




if __name__ == "__main__":
    app.run(debug=True)

