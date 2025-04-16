impares = []
pares = []

print("----- SAIBA A QUANTIDADE DE ÍMPARES E PARES -----\n")

for n in range(1,11):
    numero = int(input(f"Digite o {n}º número: "))
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
print("\n> Números Pares: ",pares)
print("> Números Ímpares: ",impares)