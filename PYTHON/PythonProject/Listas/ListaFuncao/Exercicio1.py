import math

def calcular_imc(peso,alt):
    IMC = (alt * alt) / peso
    return IMC

peso = float(input("Digite o seu peso (em kG): "))
alt = float(input("Digite a sua altura (em m): "))

resultado = calcular_imc(peso,alt)

print(f"Seu IMC é: {resultado}")