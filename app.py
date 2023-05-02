from flask import Flask, render_template, request, flash, redirect
from randomizer import choice_maker
from names import names


app = Flask(__name__)
app.config['SECRET_KEY'] = "averysecredtivekey123"

@app.route("/", methods=('GET', 'POST'))
def home():
    return render_template('home.html')

@app.route("/name", methods=('GET', 'POST'))
def name():
    if request.method == 'POST':
        print(f"this is the print: {request.method}")
        if request.form['name1'] == "":
            flash("Blank names not excepted!")
            return render_template("home.html", names=names)
        else:
            names.append(request.form['name1'])
            return render_template("home.html", names=names)
        
    choices = []
    random = choice_maker(names)
    return render_template("home.html", choices=choices, names=names, random=random)

@app.route("/random", methods=('GET', 'POST'))
def random():
    choices = []
    random = choice_maker(names)
    return render_template("home.html", choices=choices, names=names, random=random)


@app.route("/reset", methods=('GET', 'POST'))
def reset():
    names.clear()
    choices = []
    return render_template('home.html', names=[])

if __name__ == "__main__":
    app.run(debug=True)