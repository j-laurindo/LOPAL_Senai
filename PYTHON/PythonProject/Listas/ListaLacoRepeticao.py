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
"""num = int(input("Digite um número para verificar se ele é primo: "))

if num <= 1:
    print("NÚMERO INVÁLIDO")
else:
    for n in range (2,num):
        if num % n == 0:
            primo = False
            break
        else:
             primo = True
    if primo:
        print(f"{num} é um número primo")
    else:
        print(f"{num} não é um número primo")"""

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
"""print("--- CONTAGEM DE VOGAIS ---")
frase = input("Insira sua frase aqui: ")

a = 0
e = 0
i = 0
o = 0
u = 0

for letra in frase:
    if letra == "a" or letra == "A":
        a += 1
    elif letra == "e" or letra == "E":
        e += 1
    elif letra == "i" or letra == "I":
        i += 1
    elif letra == "o" or letra == "O":
        o += 1
    elif letra == "u" or letra == "U":
        u += 1

print(f"-> QUANTIDADE DE VOGAIS NA FRASE: A: {a} | E: {e} | I: {i} | O: {o} | U: {u}")"""




## A ideia é fazer um for range que utilize como parametro 
                ## o tamanho da frase toda concatenada## fazendo com que eu consiga 
                # percorrer todos os caractereres da frase e possa fazer uma contagem de
                ## todas as vogais por if e elif

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

"""quantidade = int(input("Quantos números você deseja digitar: "))
numeros = []
menores = []

for n in range(quantidade):
    num = int(input(f"Digite o {n}º número: "))
    numeros.append(num)

media = sum(numeros) / quantidade

for m in range(numeros):
    if m < media:
        menores.append(m)

print(numeros)
print(media)
print(menores)"""

# Exercício 10
"""quantidade = int(input("Quantos números você deseja digitar: "))
numeros = []
for n in range(1,quantidade+1):    
    num = int(input(f"Digite o {n}º número: "))    
    numeros.append(num)
    print(sorted(numeros))  # Sorted() é utilizado para organizar listas de maneira ordenada (https://docs.python.org/3/howto/sorting.html)
    
print("O segundo maior número é o: ",sorted(numeros)[-2])"""


## DESAFIO ##
# Exercício 1
"""print("--- SIMULAÇÃO DE POPULAÇÃO DE COELHOS ---")

coelhos_iniciais = int(input("Digite o número inicial de coelhos: "))
taxa_reproducao = float(input("Digite a taxa de reprodução (% por geração): "))
taxa_mortalidade = float(input("Digite a taxa de mortalidade (% por geração): "))
geracoes = int(input("Digite o número de gerações para simular: "))
populacao = coelhos_iniciais

for gen in range(1, geracoes + 1):
    nascimentos = populacao * (taxa_reproducao / 100)
    mortes = populacao * (taxa_mortalidade / 100)
    populacao = populacao + nascimentos - mortes
print(f"-> Na {gen}ª geração, terá uma população de: {populacao:.0f} coelhos")"""

# Exercício 2
