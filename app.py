from flask import Flask, render_template, request, session, redirect
import fiszki
import random
import os

app = Flask(__name__)

app.secret_key = "fufueyg3221921jdcz74dis8w3rgcjidhxhsi"

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

@app.route("/delete", methods=["GET", "POST"])


def delete():
    polskie, francuskie = fiszki.wczytaj_slowa()
    francuskie.sort()
    elementy = francuskie
    message=""

    if request.method == "POST":
        frword = request.form["deletefrench"]
        if frword =="":
            message = "Puste usunięcie!"
        else:
            if fiszki.check(frword)==True:
                message = "Usunięto fiszkę!"
            else:
                message = "Hasła nie ma w bazie!"
        fiszki.usun_haslo(frword)
        polskie, francuskie = fiszki.wczytaj_slowa()
        francuskie.sort()
        elementy = francuskie

    return render_template("delete.html", message=message, elementy = elementy)

@app.route("/check",  methods=["GET", "POST"])
def check():

    message=""

    if request.method == "POST":
        frword = request.form["checkword"]
        if frword =="":
            message = "Puste zapytanie!"
        else:
            if fiszki.check(frword)==True:
                message = "Fiszka jest w bazie!"
            else:
                message = "Hasła nie ma w bazie!"

    return render_template("check.html", message=message)

@app.route("/polish",methods=["GET", "POST"])
def polish():#do poprawienia - aby jak jest niepoprawna odpowiedz to losowana była kolejna fiszka
    #i aby przy braku buffora nie robił się błąd
    if not os.path.exists("wordsbufor.txt"):
        fiszki.create_buffer()
    response=""
    message=""
    definicja = ""
    polskie, francuskie = fiszki.wczytaj_buffor()
    if request.method == "GET":
        if len(francuskie) == 0:
            message = "Fiszki skończone!"
            os.remove("wordsbufor.txt")
        elif len(polskie) > 0:
            position = random.randint(0, len(polskie)-1)
            session["position"] = position
            definicja = polskie[position]
        else:
            message = "Super! Wszystkie fiszki zostały powtórzone!"      
    if request.method == "POST":
        position = session.get("position")
        definicja = polskie[position]
        response = request.form["response"]
        if response.lower() == francuskie[position].lower():
            message = "Dobrze!"
            francuskie.pop(position)
            polskie.pop(position)
            fiszki.remove_entry(position)
            return redirect("/polish")
        else:
            message = "Poprawna odpowiedź to:"+str(francuskie[position])

    return render_template("polish.html",message=message, definicja=definicja, response=response)

@app.route("/french")
def french():
    return render_template("french.html")

app.run(debug=True)