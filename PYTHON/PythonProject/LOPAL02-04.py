## LAÇO DE REPETIÇÃO: While

## Exemplo 1
"""num = 1
while num <= 10:
    print(num)
    num += 1"""
from unicodedata import numeric

## Exercício 1

"""num = int(input("Digite um número de 5 a 10: "))

while num > 0:
    print(num)
    num -= 1"""

## Exercício 2

"""maior = float(0.0)
contador = 1

while contador <= 5:
    num = float(input("Digite um número: "))
    if num > maior:
        maior = num
    contador += 1
print("O maior número é:", maior)"""

## Exercício 3
"""print("--> DESCUBRA AQUI O SEU FATORIAL <--\n")
num = int(input("Digite o número: "))
fatorial = 1

while num >= 1:
    fatorial = fatorial * num
    num -= 1
print(fatorial)"""

## Exercício 4

"""lista = int(input("Digite o tamanho da lista: "))
numeros = []
contador = 0

while contador < lista:
    numero = float(input("Digite um número: "))
    numeros.append(numero)
    contador += 1
media = sum(numeros) / lista
print("A média dos números é: ",media)"""

## Exercício 5

print("--> CALCULADORA BÁSICA <--\n")
opcao = str(input("-> Deseja iniciar a calculadora? \nResposta: "))

if opcao == "Sim":
    while opcao == "Sim":
        op = str(input("\nEscolha a operação | + (Adição); - (subtração); / (divisão); * (multiplicação): "))
        if op == "+":
            num1 = int(input("\nInsira o primeiro número: "))
            num2 = int(input("Insira o segundo número: "))
            print(f"{num1} + {num2} = ",num1 + num2)
            opcao = str(input("\nDeseja fazer a operação novamente? Resposta: "))
        elif op == "-":
            num1 = int(input("\nInsira o primeiro número: "))
            num2 = int(input("Insira o segundo número: "))
            print(f"{num1} - {num2} = ", num1 - num2)
            opcao = str(input("\nDeseja fazer a operação novamente? Resposta: "))
        elif op == "*":
            num1 = int(input("\nInsira o primeiro número: "))
            num2 = int(input("Insira o segundo número: "))
            print(f"{num1} * {num2} = ", num1 * num2)
            opcao = str(input("\nDeseja fazer a operação novamente? Resposta: "))
        elif op == "/":
            num1 = int(input("\nInsira o dividendo: "))
            num2 = int(input("Insira o divisor: "))
            print(f"{num1} / {num2} = ", num1 / num2)
            opcao = str(input("\nDeseja fazer a operação novamente? Resposta: "))
    print("\n-> Calculadora encerrada")
else:
    print("\n-> Calculadora desligada")