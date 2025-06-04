quantidade = int(input("Quantos números você deseja digitar: "))
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
print(menores)