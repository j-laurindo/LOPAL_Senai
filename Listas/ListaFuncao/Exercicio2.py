def maior_n(numeros):
    maior = max(numeros,key=float)
    print(f"O maior número digitado na lista {numeros} é: {maior}")

tam = int(input("Digite a quantidades de números que quer digitar: "))
numeros = []

for n in range(tam):
    num = float(input(f"Digite o {n+1}º número: "))
    numeros.append(num)

maior_n(numeros)
      

