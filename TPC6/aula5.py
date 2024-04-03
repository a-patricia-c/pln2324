from flask import Flask, render_template
import json

app = Flask(__name__)

with open("conceitos_v2.json", encoding="latin1") as file:
    conceitos = json.load(file)

@app.route("/")
def home():
    return render_template("Home(F).html")

@app.route("/conceitos")
def listar_conceitos():
    return render_template("conceitos.html", conceitos=conceitos)

@app.route("/conceitos/<conceito>")
def consultar_conceitos(conceito):
    return render_template("designacao.html", conceitos=conceitos, conceito=conceito, designacao=conceitos[conceito])

#app.route("/conceitos/<conceito>", methods=["PUT"])
#def editar_conceitos(conceito):
#    pass

app.run(host="localhost", port=4002, debug=True)