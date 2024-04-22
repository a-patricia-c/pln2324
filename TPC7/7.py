from flask import Flask, render_template, request
import json
import os

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
    if conceito in conceitos.keys():
        return render_template("designacao.html", conceitos=conceitos, conceito=conceito, designacao=conceitos[conceito])
    else:
        return render_template("erro.html", erro="O conceito não existe na sua base de dados.")

@app.route("/conceitos", methods=["POST"])
def adicionar_conceitos():
    designacao = request.form.get("designacao")
    descricao = request.form.get("descricao")
    en = request.form.get("en")
    print(designacao, descricao, en)
    conceitos[designacao] = {
        "desc": descricao,
        "en": en
    }
    return render_template("conceitos.html", conceitos = conceitos)


@app.route("/conceitos/<designacao>", methods=["DELETE"])
def delete_conceito(designacao):
    os.rename("conceitos_v2.json", "conceitos_backup.json")
    file_out = open("conceitos_v2.json", "w")
    json.dump(conceitos, file_out, indent=4, ensure_ascii=False)
    file_out.close()
    del conceitos[designacao]
    return render_template("conceitos.html", conceitos=conceitos)

@app.route("/pesquisar_conceitos", methods=["GET"])
def procurar_conceitos():
    search_term = request.args.get('q', '')
    results = {}
    if search_term:
        for key, value in conceitos.items():
            if search_term.lower() in key.lower() or search_term.lower() in value['desc'].lower() or search_term.lower() in value['en'].lower():
                results[key] = value
    else:
        results = conceitos
    return render_template("conceitos.html", conceitos=conceitos, results=results)

@app.route("/table")
def table():
    return render_template("table.html", conceitos=conceitos)

app.run(host="localhost", port=4002, debug=True)
