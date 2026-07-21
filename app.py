from flask import Flask, render_template, request
import fiszki

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/flashcards")
def flashcards():
    return render_template("flashcards.html")

@app.route("/add", methods=["GET", "POST"])
def add():

    message=""

    if request.method == "POST":
        frword = request.form["addfrench"]
        plword = request.form["addpolish"]
        fiszki.dodaj_haslo(plword, frword)
        if frword =="" or plword =="":
            message = "Puste hasło!"
        else:
            message = "Dodano fiszkę!"
    return render_template("add.html", message=message)

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