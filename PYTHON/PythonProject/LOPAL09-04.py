## WHILE TRUE
# Quando usar: 1) VocÊ não sabe quantas vezes vai repetir; 2)A condição de parada acontece dentro...

while True:
    resposta = input("Digite 'sair' para encerrar: ")
    if resposta == "sair":
        break

## FOR CONTINUE
# Objetivo: Mostrar como pular repetições específicas. Ele não encerra o laço, só pula aquela volta

"""for i in range(5):
    if i == 2:
        continue
    print(i)"""

