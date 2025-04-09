## LISTA EXERCÍCIOS -- Estrutura de Decisão e Teste de Mesa

## Exercício 1
"""ano = int(input("Digite um ano qualquer: "))

if (ano % 4 == 0) and (ano % 100 != 0) or (ano % 4 != 0) and (ano % 400 == 0) or (ano % 4 == 0) and (ano % 400 == 0):
    print(f"{ano} é bissexto!")
else:
    print(f"{ano} não é bissexto!")"""

## Exercício 2
"""altura = float(input("Insira o valor da sua altura (em metros): "))
peso = float(input("Insira o valor do seu peso (em Kgs): "))

IMC = peso / altura ** 2
ImcFormatado = "%.2f" % IMC

if IMC <= 18.5:
    print(f"IMC = {ImcFormatado}  |   Valor: Baixo Peso")
elif IMC <= 24.9:
    print(f"IMC = {ImcFormatado}  |   Valor: Normal")
elif IMC <= 29.9:
    print(f"IMC = {ImcFormatado}  |   Valor: Sobrepeso")
elif IMC <=34.9:
    print(f"IMC = {ImcFormatado}  |   Valor: Obesidade")
else:
    print(f"IMC = {ImcFormatado}  |   Valor: Obesidade Mórbida")"""

## Exercício 3
"""valor = float(input("Insira o valor por unidade (em R$): "))
qtd = int(input("Insira a quantidade de produtos: "))

if qtd > 100:
    desc = valor * (10 / 100)
    total = qtd * (valor - desc)
    print(f"Valor Inicial: {valor}  |  Quantidade: {qtd}  | Desconto por unidade: {desc}  | Total com Desconto: {total} | ")
else:
    desc = valor * (5 / 100)
    total = qtd * (valor - desc)
    print(f"Valor Inicial: {valor}  |  Quantidade: {qtd}  | Desconto por unidade: {desc}  | Total com Desconto: {total} | ")"""

## Exercício 4
"""print(f"---> VERIFICAÇÃO DE VOTOS (obrigatório, facultativo, não eleitor <---\n")
idade = int(input("Digite a sua idade: "))

if idade >= 16 and idade < 18 or idade >= 70:
    print(f"Seu voto eleitoral é: FACULTATIVO")
elif idade >= 18:
    print(f"Seu voto eleitoral é: OBRIGATÓRIO")
else:
    print(f"Seu voto eleitoral é: NÃO ELEITOR")"""

## Exercício 5
"""idade1 = int(input("Insira a primeira idade: "))
idade2 = int(input("Insira a segunda idade: "))
idade3 = int(input("Insira a terceira idade: "))

if idade1 > idade2 and idade1 > idade3:
    if idade2 < idade3:
        print(f"Maior Idade: {idade1}  |  Menor Idade: {idade2}")
    else:
        print(f"Maior Idade: {idade1}  |  Menor Idade: {idade3}")
elif idade2 > idade1 and idade2 > idade3:
    if idade1 < idade3:
        print(f"Maior Idade: {idade2}  |  Menor Idade: {idade1}")
    else:
        print(f"Maior Idade: {idade2}  |  Menor Idade: {idade3}")
elif idade3 > idade1 and idade3 > idade2:
    if idade1 < idade2:
        print(f"Maior Idade: {idade3}  |  Menor Idade: {idade1}")
    else:
        print(f"Maior Idade: {idade3}  |  Menor Idade: {idade2}")"""

## Exercício 6
"""print(f"---> VERIFICAÇÃO DE HORA VÁLIDA <---\n")

hora = int(input("Insira o valor da hora: "))
minutos = int(input("Insira o valor dos minutos: "))
segundos = int(input("Insira o valor dos segundos: "))

if (hora >= 0 and hora < 24) and (minutos >= 0 and minutos < 60) and (segundos >=0 and segundos < 60):
    print(f"Resposta: HORA VÁLIDA!")
else:
    print(f"Resposta: HORA INVÁLIDA")"""

## Exercício 7
"""nota = int(input("Insira a sua nota: "))

if nota == 10 or nota >= 9:
    print(f"Nota = A")
elif nota >= 7 and nota < 9:
    print(f"Nota = B")
elif nota >= 5 and nota < 7:
    print(f"Nota = C")
elif nota >= 3 and nota < 5:
    print(f"Nota = D")
elif nota < 3 and nota < 3:
    print(f"Nota = E")
else:
    if nota > 10:
        print(f"Número inválido")"""

## Exercício 8
"""print(f"---> VERIFICAÇÃO DE QUADRADO OU RETÂNGULO <---\n")

lado1 = float(input("Insira o valor do primeiro lado: "))
lado2 = float(input("Insira o valor do segundo lado: "))
lado3 = float(input("Insira o valor do terceiro lado: "))
lado4 = float(input("Insira o valor do quarto lado: "))

if (lado1 == lado2 and lado3 == lado4) and (lado2 == lado3 and lado1 == lado4) and (lado2 == lado4 and lado1 == lado3):
    print(f"Essa figura é: QUADRADO")
elif (lado1 == lado2 and lado3 == lado4 and lado3 != lado1 and lado4 != lado1) or (lado1 == lado3 and lado2 == lado4 and lado1 != lado2 and lado4 != lado3):
    print(f"Essa figura é: RETÂNGULO")
else:
    print(f"Essa figura é: NENHUM DOS DOIS")"""

## Exercício 9
"""print(f"---> CALCULADORA SIMPLES <---\n")

n1 = float(input("Insira o primeiro número (com casa decimal): "))
n2 = float(input("Insira o segundo número (com casa decimal): "))
escolha = str(input("Escolha qual operação que quer realizar entre número 1 e número 2  \n|  + -> Adição | - ~> Subtração | * -> Multiplicação | / -> Divisão : "))

if escolha == "+":
    print(f"A soma entre {n1} e {n2} é:", n1+n2)
elif escolha == "-":
    print(f"A subtração entre {n1} e {n2} é:", n1 - n2)
elif escolha == "*":
    print(f"A multiplicação entre {n1} e {n2} é:", n1 * n2)
elif escolha == "/":
    print(f"A divisão entre {n1} e {n2} é:", n1 / n2)
else:
    print(f"Opção Inválida")"""

## Exercício 10
"""print(f"---> Calculadora de Média com Descarte de Notas <---\n")

nota1 = float(input("Insira a nota da primeira prova: "))
nota2 = float(input("Insira a nota da segunda prova: "))
nota3 = float(input("Insira a nota da terceira prova: "))

if nota1 < nota2 and nota1 < nota3:
    media = (nota2 + nota3) / 2
    print(f"A média é: {media}")
elif nota2 < nota1 and nota2 < nota3:
    media = (nota1 + nota3) / 2
    print(f"A média é: {media}")
else:
    media = (nota1 + nota2) / 2
    print(f"A média é: {media}")"""

## Exercício 12 - DESAFIO
"""import random

print("---> JOGO DE ADIVINHAÇÃO <--- \n> Entre em uma competição com a máquina e tente adivinhar qual número ela escolherá de 1 a 10")
chute = int(input("Digite o seu chute: "))
computador = random.randint(1, 10)

if chute != computador:
    if chute > computador:
        print(f"{chute} é maior que o computador")
    else:
        print(f"{chute} é menor que o computador")
    print("Você tem mais uma tentativa!")

    SegundoChute = int(input("\nDigite o seu segundo chute: "))

    if SegundoChute == computador:
        print("\nVocê ganhou!\n")
        print(f"- Primeiro chute: {chute} \n- Segundo chute: {SegundoChute} \n- Escolha do computador:{computador}")
    else:
        print("\nVocê perdeu!\n")
        print(f"- Primeiro chute: {chute} \n- Segundo chute: {SegundoChute} \n- Escolha do computador:{computador}")
else:
    print("\nVocê ganhou!\n")
    print(f"- Primeiro chute: {chute} \n- Escolha do computador: {computador}")"""

a = 8
b = 3
if a > b:
    a = a - 2

print(a)
b = b + a
print(a, b)
