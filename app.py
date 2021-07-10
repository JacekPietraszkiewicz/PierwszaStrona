from flask import Flask
from flask import request, render_template, redirect


app = Flask(__name__)

@app.route('/message', methods=['GET', 'POST'])
def message():
    if request.method == 'GET':
        return render_template("form.html", items = items, errors = errors)
    elif request.method == 'POST':
        f = open("formatka", "a")
        f.write(request.form["firstname"]+"\n")
        f.close()
        return render_template("thanks.html", kto = request.form["firstname"], errors = "Błędy")

