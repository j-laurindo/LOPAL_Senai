contador = 0

print("--> DESCUBRA QUANTOS NÚMEROS (de 10 tentativas) SÃO MÚLTIPLOS DE 3 <--\n")
for n in range(1,11):
    num = float(input(f"{n}) Digite um número: "))
    if num % 3 == 0:
        contador += 1
if contador > 0:
    print(f"\n-> Foram digitados {contador} número(s) múltiplos de 3!")
else:
    print("\n-> Nenhum número digitado é múltiplo de 3 :(")