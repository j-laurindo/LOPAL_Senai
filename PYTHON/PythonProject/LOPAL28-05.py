# Arquivo TXT
"""with open("meu_arquivo.txt", "w", encoding='utf-8')as arquivo:
    arquivo.write("Olá mundo!\n")
    arquivo.write("Aprendendo Python\n")

with open("meu_arquivo.txt", "r") as arquivo:
    print(arquivo.read())"""

# Arquivo CSV
"""import csv

with open("produtos.csv", "w", newline="", encoding='utf-8') as csvfile:
    texto = csv.writer(csvfile, delimiter=" ", quotechar="|", quoting=csv.QUOTE_MINIMAL)
    texto.writerow(['Nome','Preço'])
    texto.writerow(['Livro', '20'])

with open("produtos.csv", "r", newline="", encoding='utf-8') as csvfile:
    leitor = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for linha in leitor:
        print(" | ".join(linha))"""

# Arquivo JSON
"""import json

#dados que serão escritos no arquivo json
informacoes = {
    "Nome": "Julia",
    "Idade": "19 anos"
}

with open("dados.json", "w", encoding='utf-8') as arquivo:
    json.dump(informacoes, arquivo)

with open("dados.json", "r", encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

print(dados)"""

# Arquivo XML

# xml_str = """<?xml version="1.0" encoding="UTF-8"?>
# <config>
#    <versao>1.0</versao>
# </config>
"""
with open("config.xml", "w", encoding="UTF-8") as f:
    f.write(xml_str)

with open("config.xml", "r", encoding="UTF-8") as f:
    conteudo = f.read()
    print(conteudo)"""

# Arquivo Excel

import pandas 

