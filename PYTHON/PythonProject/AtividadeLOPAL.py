#Exercício 1
"""
n1 = int(input("Digite um primeiro número: "))
n2 = int(input("Digite um segundo número: "))

resultado = n1 + n2

print(f"O resultado da soma é igual a: {resultado}")
"""
############################################################

#Exercício 2
"""
num = int(input("Insira um número para identificar se ele é ímpar: "))
result = (num % 2 == 1)

print(f"Ímpar -> True  |  Par -> False  |  Resultado : {result}")
"""
############################################################

# Exercício 3
"""
print(f"- Verifique se: 1º Valor > 3 ou se o 2º Valor < 4")
n1 = int(input("Digite o 1º valor: "))
n2 = int(input("Digite o 2º valor: "))
result = (n1 > 3 or n2 < 4)

print(f"Verdadeira -> True  |  Falso -> False  |  Resultado: {result}")
"""
############################################################

# Exercício 4
"""
num = int(input("Digite um número: "))
valor_absoluto = abs(num)

print(f"O valor absoluto de {num} é: {valor_absoluto}")
"""
#############################################################

# Exercício 5
"""
n1 = int(input("Insira o primeiro número: "))
n2 = int(input("Insira o segundo número: "))

result1 = n1 % 2 == 0
print(f"\n-- VERIFICAÇÃO 1º NÚMERO --")
print(f"True = É par | False = É ímpar : {result1} ")

result2 = n2 % 2 == 0
print(f"\n-- VERIFICAÇÃO 1º NÚMERO --")
print(f"VERIFICAÇÃO 2º NÚMERO -- True = É par | False = É ímpar : {result2} ")
"""
################################################################
"""
# Exercício 6

n1 = int(input("Insira o primeiro número: "))
n2 = int(input("Insira o segundo número: "))

result = n1 and n2 < 0

print(f"\n-- VERIFICAÇÃO --\n > Os dois valores são negativos?\nTrue = É negativo | False = É positivo : {result}")
"""
##################################################################
"""
#Exercício 7

n1 = float(input("Insita o primeiro valor: "))
n2 = float(input("Insita o segundo valor: "))
n3 = float(input("Insita o terceiro valor: "))

result = (n1 + n2 + n3) / 3

print(f"\nA média dos valores é: {result}")
"""
##################################################################
"""
# Exercício 8

n1 = int(input("Insira o primeiro valor: "))
n2 = int(input("Insita o segundo valor: "))

result = n1 + 15 == n2 * 3

print(f"\n-- VERIFICAÇÃO -- \nTrue = Valor 1 + 15 for igual a Valor 2 * 3 \nFalse = Não for igual \nResultado: {result}")
"""
####################################################################
"""
# Exercício 9

dividendo = int(input("Insira o valor que você quer dividir (dividendo): "))
divisor = int(input("Insira o valor pelo qual vai ser dividido (divisor): "))
resto = dividendo % divisor

DivResult = dividendo / divisor
Result1 = resto / dividendo
Result2 = resto / divisor
Result3 = DivResult / dividendo
Result4 = DivResult / divisor

print(f"\n-> O resultado da divisão é: {DivResult}")
print(f"-> Divisão entre Resto da Divisão X Dividendo = {Result1}")
print(f"-> Divisão entre Resto da Divisão X Divisor = {Result2}")
print(f"-> Divisão entre Resultado X Dividendo = {Result3}")
print(f"-> Divisão entre Resultado X Divisor = {Result4}")
"""
########################################################################

# Exercício 10
"""
num = int(input("Insira o valor em º: "))
convert = (num * 1.8) + 32

print(f"A conversão para Fahrenheit é: F = {convert}")
"""
#########################################################################

# Exercício 11
"""
altura = float(input("Insira a sua altura em metros (m): "))
peso = float(input("Insira o seu peso em quilos (kg): "))

imc = peso / altura ** 2
formatacao = "{:.2f}".format(imc)

print(f"Seu IMC é: {formatacao}")
"""
##########################################################################
"""
# Exercício 12

nota1 = float(input("Insira a 1ª Nota: "))
nota2 = float(input("Insira a 2ª Nota: "))
nota3 = float(input("Insira a 3ª Nota: "))

peso1 = int(input("\nInsira o 1º Peso: "))
peso2 = int(input("Insira o 1º Peso: "))
peso3 = int(input("Insira o 1º Peso: "))

media = ((nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)) / (peso1 + peso2 + peso3)

print(f"\nA média ponderada é: {media}")
"""
#########################################################################
"""
# Exercício 13

print(f"-- REALIZE UM CÁLCULO DE POTÊNCIA! --")

num = int(input("Insira o valor do número a ser potenciado: "))
expo = int(input("Insira o valor do expoente: "))

print(f"O valor da potenciação é: ", pow(num, expo))
"""
##########################################################################

# DESAFIOS

"""
# Exercício 1
print(f"-- REALIZE UM CÁLCULO DE RAIZ CUBICA! --")
num = int(input("\nInsira um número: "))

raiz = num ** (1 / 3)
formatacao = "{:.2f}".format(raiz)

print(f"O resultado é: {formatacao}")
"""

"""# Exercício 2

print(f"-- REALIZE UM CÁLCULO DE MONTANTE DE JUROS COMPOSTOS! --")

capital = float(input("\nInsira a quantidade de capital (R$): "))
TaxaJuros = float(input("Insira a taxa de juros: "))
tempo = float(input("Insira o tempo (em anos): "))

montante = capital * ((1 + TaxaJuros) ** tempo)
formatacao = "{:.2f}".format(raiz)


print(f"O montante de juros compostos é igual a: {formatacao}")"""


