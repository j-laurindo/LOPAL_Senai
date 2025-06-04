## RAIOS DE CONJUNTO - FOR
## Exemplo: Listas

"""frutas = ['maçã', 'banana', 'laranja']
for fruta in frutas:
    print(fruta)
print(frutas[0])"""

## Exemplo: String

"""mensagem = 'Hello World!'
for caractere in mensagem:
    print(caractere)
"""

## Exemplo: Tuplas

"""cores = ('Vermelho', 'Amarelo', 'Verde', 'Azul')
for cor in cores:
    print("Cor:",cor)"""

## Exemplo: Dicionário

"""pessoa = {
    "nome":"Julia",
    "idade":"18",
    "profissão":"desenvolvedora de sistemas"
}
print(pessoa["nome"])
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")

    ## MOSTRANDO SOMENTE UM CONJUNTO DO DICIONÁRIO
for chave, valor in pessoa.items():
    if chave == "nome":
        print(f"{chave}: {valor}")
    print("Acabou o IF")
print("Acabou o FOR")"""

    ## DICIONÁRIO DENTRO DE DICIONÁRIO
"""alunos = {
    "123": {
        "nome":"Lucas",
        "idade":"17",
    },
    "456": {
        "nome":"Maria",
        "idade":"18"
    }
}
print(alunos["456"]["nome"])
for ra, dados in alunos.items():
    print(f"RA: {ra}")
    for chave, valor in dados.items():
        print(f"{chave.capitalize()}: {valor}")"""

## Exemplo: Conjuntos

"""animais = {"gato", "cachorro", "elefante", "girafa"}
for animal in animais:
    print("Animal:", animal)"""

## Exemplo: Range

"""for numero in range(5):
    print(numero)
for numero in range (1,11):
    print(numero)
for numero in range (0,11,2):
    print(numero)
for numero in range (0,11,3):
    print(numero)"""

## Exemplo: Arquivo

"""nome_arquivo = "C:/Users/49147341840/Desktop/arquivo.txt"
with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        print(linha.strip())"""

####### EXERCÍCIOS #######

## Exercício 1

"""for numero in range(0,11,2):
    print(numero)"""

## Exercício 2

"""cores = ['Vermelho','Azul','Verde','Amarelo']

for cor in cores:
    print("Cor:", cor)"""

## Exercício 3
"""soma = 0

for numero in range(1,101):
    soma = soma + numero
print(soma)"""

## Exercício 4

"""num = int(input("Insira um valor na qual deseja saber a tabuada: "))
tabuada = 1

for n in range(1, 11):
    tabuada = num * n
    print(f"{num} x {n} =", tabuada)"""

## Exercício 5

"""num = int(input("Digite quantas notas serão calculadas: "))

for x in range(1, num + 1):
    print(x)
"""
