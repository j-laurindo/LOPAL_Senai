def eh_primo(num):
    if num <= 1:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False
    return True 

num = int(input("Digite um número e saiba se ele é primo: "))
resultado = eh_primo(num)

print(f"True = É primo  |   False = Não é primo \nRESULTADO: {resultado}")
