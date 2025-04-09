# Exercício 1

"""contador = 0

print("--> DESCUBRA QUANTOS NÚMEROS (de 10 tentativas) SÃO MÚLTIPLOS DE 3 <--\n")
for n in range(1,11):
    num = float(input(f"{n}) Digite um número: "))
    if num % 3 == 0:
        contador += 1
if contador > 0:
    print(f"\n-> Foram digitados {contador} número(s) múltiplos de 3!")
else:
    print("\n-> Nenhum número digitado é múltiplo de 3 :(")"""

# Exercício 2

"""print("-> ENTRE NO NOSSO SISTEMA COM A SUA SENHA <-\n")
while True:
    senha = input("Digite sua senha: ")
    senha_correta = "123py"
    if senha == senha_correta:
        print("\n-> BEM VINDO(A)!")
        break"""

# Exercício 3

"""print("---- VENHA CONHECER O NOSSO MENU DE COMIDAS!!-----")

while True:
    print("\n\n---- NOSSO MENU ----")
    print("-> 1) Macarrão a Bolanhesa")
    print("-> 2) Risoto de Camarão")
    print("-> 3) Esfihas de Carne")
    print("-> 4) Lasanha ao Molho Branco")
    resposta = input("\nDigite 'sair' caso queira encerrar: ")
    opcao = resposta.lower()

    if opcao == "sair":
        break"""

# Exercício 4

# Exercício 5

"""tentativa = 1

print("--- ENTRE NO NOSSO SISTEMA ---")
while tentativa <= 3:
    senha = input("\nDigite sua senha: ")
    senha_correta = "123py"
    if senha == senha_correta:
        break
    else:
        tentativa += 1
if tentativa > 3:
    print("\n-> ACESSO BLOQUEADO")
else:
    print("\n-> ACESSO PERMITIDO")"""


# Exercício 6

"""impares = []
pares = []

print("----- SAIBA A QUANTIDADE DE ÍMPARES E PARES -----\n")

for n in range(1,11):
    numero = int(input(f"Digite o {n}º número: "))
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
print("\n> Números Pares: ",pares)
print("> Números Ímpares: ",impares)"""

# Exercício 7

# Exercício 8
"""import random

lados = ["cara","coroa"]
contagem = 0

while contagem < 3:
    opcao = random.choice(lados)    # essa linha vai deixar aleatorizar as escolhas em todas as repetições
    if opcao == "cara":
        contagem += 1
    elif opcao != "cara":
        contagem -= contagem    # essa linha anula a contagem caso a próxima repeição não for cara
    print(opcao)"""

# Exercício 9

quantidade = int(input("Quantos números você deseja digitar: "))
numeros = []
menores = []

for n in range(quantidade):
    num = int(input(f"Digite o {n}º número: "))
    numeros.append(num)

media = sum(numeros) / quantidade

"""for m in range(numeros):
    if m < media:
        menores.append(m)"""

print(numeros)
print(media)
"""print(menores)"""
