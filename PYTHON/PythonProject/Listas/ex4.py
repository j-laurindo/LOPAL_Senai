num = int(input("Digite um número para verificar se ele é primo: "))

if num <= 1:
    print("NÚMERO INVÁLIDO")
else:
    for n in range (2,num):
        if num % n == 0:
            primo = False
            break
        else:
             primo = True
    if primo:
        print(f"{num} é um número primo")
    else:
        print(f"{num} não é um número primo")