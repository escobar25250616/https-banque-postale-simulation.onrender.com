from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Identifiants corrects
CORRECT_ID = "0840405208"
CORRECT_PWD = "petitlapin"

@app.route("/", methods=["GET", "POST"])
def login():
    erreur = None
    if request.method == "POST":
        user_id = request.form.get("identifiant")
        password = request.form.get("motdepasse")
        if user_id == CORRECT_ID and password == CORRECT_PWD:
            return redirect("/bloque")
        else:
            erreur = "Identifiant ou mot de passe incorrect."
    return render_template("login.html", erreur=erreur)

@app.route("/bloque")
def bloque():
    return render_template("bloque.html")

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
