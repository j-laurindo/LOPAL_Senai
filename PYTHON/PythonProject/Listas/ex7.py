print("--- CONTAGEM DE VOGAIS ---")
frase = input("Insira sua frase aqui: ")

a = 0
e = 0
i = 0
o = 0
u = 0

for letra in frase:
    if letra == "a" or letra == "A":
        a += 1
    elif letra == "e" or letra == "E":
        e += 1
    elif letra == "i" or letra == "I":
        i += 1
    elif letra == "o" or letra == "O":
        o += 1
    elif letra == "u" or letra == "U":
        u += 1

print(f"-> QUANTIDADE DE VOGAIS NA FRASE: A: {a} | E: {e} | I: {i} | O: {o} | U: {u}")