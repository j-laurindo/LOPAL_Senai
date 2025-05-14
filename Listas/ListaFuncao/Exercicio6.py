def contar_vogais(frase):
    frase = frase.lower()
    contador = {}
    vogais = 'aeiou'
    
    for letra in vogais:
        if letra in frase:
            contador[letra] = frase.count(letra)
    return contador


frase = input("Digite uma frase: ")
print(f"-> Frase Original: {frase} \n-> Quantidade de vogais: {contar_vogais(frase)}")
