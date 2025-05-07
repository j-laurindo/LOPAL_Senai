quantidade = int(input("Quantos números você deseja digitar: "))
numeros = []
for n in range(1,quantidade+1):    
    num = int(input(f"Digite o {n}º número: "))    
    numeros.append(num)
    print(sorted(numeros))  # Sorted() é utilizado para organizar listas de maneira ordenada (https://docs.python.org/3/howto/sorting.html)
    
print("O segundo maior número é o: ",sorted(numeros)[-2])