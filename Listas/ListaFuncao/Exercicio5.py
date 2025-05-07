def eh_primo(num):
    if num is not (num % num == 0) and (num % 1 == 0):
        num = False
    else:
        num = True
    return num

num = int(input("Digite um número e saiba se ele é primo: "))
resultado = eh_primo(num)

print(f"True = É primo  |   False = Não é primo \nRESULTADO: {resultado}")

## CORRIGIR ERRO