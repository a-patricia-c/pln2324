from deep_translator import GoogleTranslator
import json

file = open("conceitos.json", encoding="utf-8")
conceitos = json.load(file)

novo_dici = {}

i = 0
for designacao_pt in conceitos:
    print(i)
    designacao_en = GoogleTranslator(source='pt', target='en').translate(designacao_pt)
    novo_dici[designacao_pt] = {"desc": conceitos[designacao_pt], "en": designacao_en}
    i = i + 1

file_out= open ("conceitos_v2.json", "w")
json.dump(novo_dici, file_out, indent=4, ensure_ascii=False)
