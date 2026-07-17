from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/flashcards")
def flashcards():
    return render_template("flashcards.html")

@app.route("/add")
def add():
    return render_template("add.html")

@app.route("/delete")
def delete():
    return render_template("delete.html")

@app.route("/check")
def check():
    return render_template("check.html")

@app.route("/polish")
def polish():
    return render_template("polish.html")

@app.route("/french")
def french():
    return render_template("french.html")

app.run(debug=True)