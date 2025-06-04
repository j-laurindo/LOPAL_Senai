# Estrutura da função

"""def nome_da_funcao(parametro1, parametro2):
    # corpo da função
    instruções"""
import pep8

## Primeiras funções
### Função Saudação
"""def saudacao():
    print("Olá mundo!")

saudacao()"""

### Função Média
"""def calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media

nota1 = int(input("Insira a primeira nota: "))
nota2 = int(input("Insira a segunda nota: "))

resultado = calcular_media(nota1, nota2)

print(f"A média entre as notas {nota1} e {nota2} é: {resultado}")"""

### Variável Local
"""É uma variável criada dentro da função só existe dentro da função, ela deixa de existir quando a função termina"""
"""def minha_funcao():
    x = 10
    print(x)

minha_funcao()
print(x)"""

### Variável Global
"""É a variável criada fora de qualquer função e existe em todo programa. Pode ser usada dentro das funções,
   mas não pode ser alterada dentro delas sem um comando especial"""

"""y = 20
def outra_funcao():
    print(y)

outra_funcao()
print(y)
"""

"""def mudar_valor():
    global z
    z = 100

z = 5
mudar_valor()
print(z)"""

### None
"""None é um valor especial que representa "nada", "sem valor" ou "ausencia de retorno". Isso ocorre quando uma função
   não tem um return"""

"""def diz_ola():
    print("Olá!")

resultado = diz_ola()
print(resultado)"""

#################################################################
###### EXERCÍCIOS ###############################################

# Exercício 1
"""def calcular_dobro(num):
    dobro = num * 2
    return dobro

num = int(input("Digite um número: "))

resultado = calcular_dobro(num)
print(f"O dobro de {num} é: {resultado}")"""

# Exercício 2
"""def maior_valor(num1,num2):
    if num1 > num2:
        print(f"{num1} foi o maior número digitado!")
    else:
        print(f"{num2} foi o maior número digitado!")

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

maior_valor(num1,num2)"""

"""def maior_valor(num1,num2):
    if num1 > num2:
        return num1
    else:
        return num2

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
print(f"O maior número entre {num1} e {num2} é:",maior_valor(num1,num2))"""

# Exercício 3

"""def calcular_media(numeros):
    media = sum(numeros) / tam
    return media

tam = int(input("Digite qual é o tamanho desejado para a lista de números: "))
numeros = []

for n in range(tam):
    num = int(input(f"Digite o {n+1}º número: "))
    numeros.append(num)

resultado = calcular_media(numeros)

print(f"A média dos números {numeros} é: {resultado:.2f}")"""

# Exercício 4

"""def calcular_fatorial(numero):
    fatorial = 1

    for i in range(1, numero + 1):
        fatorial *= i
    return fatorial

numero = int(input("Digite um número para calcular o fatorial: "))
resultado = calcular_fatorial(numero)

print(f"O fatorial de {numero} é: {resultado}")"""
