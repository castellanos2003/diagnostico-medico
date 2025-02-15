from flask import Flask, render_template, request
from motor import obtener_diagnostico

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    diagnostico = None

    if request.method == "POST":
        sintomas = request.form.get("sintomas").split(",")
        diagnostico = obtener_diagnostico(sintomas)

    return render_template("index.html", diagnostico=diagnostico)

# Modificación para Vercel
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
