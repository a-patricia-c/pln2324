import re

file = open("dicionario_medico.txt", encoding="utf-8")
texto = file.read()

#data cleaning
texto = re.sub(r'\n?\f', "", texto)

#marcar designações
texto = re.sub(r'\n\n(.+)', r'\n\n@\1', texto)

termos = []
termos = re.findall(r'@(.+)\n([^@]+)', texto)


# HTML
título = "<div style='border: 10px solid #40e0d0; padding: 2px; border-radius:15px; box-shadow:0 4px 8px rgba(0,0,0,0.1); background-color: #40e0d0;'><h1 style= 'text-align: center;'color: #000;'>Dicionário Médico</h1></div>"
descrição = "<p style='text-align: center; color: #000;'>Dicionário médico desenvolvido na disciplina de PLNEB</p></div>"

body_style = ("font-size: 20px;")

body = "<body style='" + body_style + "'>"
for termo in termos:
    body += f"<h5> {termo[0]} </b></h5>"
    body += f"<p> {termo[1]} </p>"
    body += "<hr>"

body += "<body>"
html = título + descrição + body


file_out = open("aula3.html", "w")
file_out.write(html)
file_out.close()
