## IF, Teste de Mesa, Repetição

##Estrutura de Decisão

"""

if --> Se (cria condicionais)
else --> Senão (não tem condicional)
elif = else if --> Senão se (adiciona condicionais)


- SINTAXE

if condicional:
    (conteúdo da estrutura)
else
    (conteúdo da estrutura)

"""

"""## Exercício 1

idade = int(input("Escreva a sua idade: "))

if idade >= 18:
    print(f"Você é maior de idade!")
else:
    print(f"Você é menor de idade!")
"""

"""## Exercício 2

nota = float(input("Digite sua nota para avaliar seu desempenho: "))

if nota >= 9.0:
    print(f"Você foi excelente!")
elif nota >= 7.0:
    print(f"Você foi bom(a)!")
elif nota >= 5.0:
    print(f"Você foi médio(a).")
else:
    print(f"Nota insuficiente.")"""

"""## Exercício 3

num = int(input("Insira um número: "))

if num % 2 == 0:
    print(f"Você digitou um número par!")
    if num % 3 == 0:
        print(f"Além de par, ele é múltiplo de 3!")
    elif num % 5 == 0:
        print(f"Além de par, ele é múltiplo de 5!")
    else:
        print(f"Ele não é múltiplo de 3 e 5.")
elif num % 2 != 0:
    print(f"O número que você digitou é ímpar!")
    if num % 3 == 0:
        print(f"Além de par, ele é múltiplo de 3!")
    elif num % 5 == 0:
        print(f"Além de par, ele é múltiplo de 5!")
    else:
        print(f"Ele não é múltiplo de 3 e 5.")"""

"""## Exercício 4

n1 = int(input("Insira o primeiro número: "))
n2 = int(input("Insira o segundo número: "))

if n1 > n2:
    print(f"{n1} é o maior valor digitado!")
elif n2 > n1:
    print(f"{n2} é o maior valor digitado!")
else:
    print(f"Os números são iguais")"""

"""## Exercicio 5

idade = int(input("Insira uma idade: "))

if idade < 2:
    print(f"-> Bebê")
elif idade < 12:
    print(f"-> Criança")
elif idade < 18:
    print(f"-> Adolescente")
elif idade < 60:
    print(f"-> Adulto")
elif idade >= 60:
    print(f"-> Idoso")"""

"""## Exercício 6
print(f"----- CONVERSOR DE TEMPERATURA -----")
print(f"Escolha se você quer converter: \n\n1: Fahrenheit -> Celsius   |   2: Celsius -> Fahrenheit")
op = int(input("\nDigite qual é a sua escolha: "))

if op == 1:
    fah = int(input("Digite o valor em fahrenheit: "))
    cel = (fah * 9/5) + 32
    print(f"A conversão de fahrenheit para celsius é: º{cel}")
elif op == 2:
    cel = int(input("Digite o valor em celsius: "))
    fah = (cel - 32) * 5/3
    print(f"A conversão de fahrenheit para fahrenheit é: º{fah}")
else:
    print(f"Opção Inválida")
"""

"""## Exercício 7
print(f"----- TRIÂNGULOS -----")
n1 = int(input("Insira o valor do primeiro lado: "))
n2 = int(input("Insira o valor do segundo lado: "))
n3 = int(input("Insira o valor do terceiro lado: "))

if (n1 + n2) > n3 and (n1 + n3) > n2 and (n2 + n3) > n1:
    if n1 == n2 and n1 == n3:
        print(f"Os lados indicam um triângulo equilátero!")
    elif n1 != n2 and n1 != n3 and n2 != n3:
        print(f"Os lados indicam um triângulo escaleno!")
    else:
        print(f"Os lados indicam um triângulo isóceles")
else:
    print(f"Os lados não indicam um triângulo")"""


"""## Exercício 8
print(f"---> PYTHON BANK <---")
print(f"Confira se você é elegível para empréstimos em nosso banco.")

idade = int(input("Digite a sua idade: "))
renda = float(input("Digite a sua renda mensal: "))

if idade >= 18:
    if renda >= 1500:
        print(f"\nVocê está elegível para pedir empréstimos!")
    else:
        print(f"\nVocê não está elegível a empréstimos, pois sua renda mensal é menor que R$1.500,00")
elif idade < 18:
    if renda >= 1000:
        print(f"\nVocê está elegível para pedir empréstimos!")
    else:
        print(f"\nVocê não está elegível a empréstimos pois sua renda mensal é menor que R$1.000,00")"""

## Exercício 9
"""import random
print(f"---> PEDRA, PAPEL E TESOURA <---")
escolha = str(input("Escreva qual será a sua jogada (pedra, papel ou tesoura): ")).upper()
opcoes = ["PEDRA", "PAPEL", "TESOURA"]
computador = random.choice(opcoes)

print(f"Sua resposta: {escolha}   |   Escolha do computador: {computador}\n")

if escolha == "PEDRA":
    if computador == "PEDRA":
        print(f"Empatou! {escolha} X {computador}")
    elif computador == "TESOURA":
        print(f"Ganhou! {escolha} X {computador}")
    else:
        print(f"Perdeu! {escolha} X {computador}")
elif escolha == "PAPEL":
    if computador == "PEDRA":
        print(f"Ganhou! {escolha} X {computador}")
    elif computador == "PAPEL":
        print(f"Empatou! {escolha} X {computador}")
    else:
        print(f"Perdeu! {escolha} X {computador}")
elif escolha == "TESOURA":
    if computador == "PEDRA":
        print(f"Perdeu! {escolha} X {computador}")
    elif computador == "PAPEL":
        print(f"Ganhou! {escolha} X {computador}")
    else:
        print(f"Empatou! {escolha} X {computador}")
else:
    print(f"Nenhum dos valores conta")"""

