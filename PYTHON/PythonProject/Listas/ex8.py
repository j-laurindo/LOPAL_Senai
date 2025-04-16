import random

lados = ["cara","coroa"]
contagem = 0

while contagem < 3:
    opcao = random.choice(lados)    # essa linha vai deixar aleatorizar as escolhas em todas as repetições
    if opcao == "cara":
        contagem += 1
    elif opcao != "cara":
        contagem -= contagem    # essa linha anula a contagem caso a próxima repeição não for cara
    print(opcao)