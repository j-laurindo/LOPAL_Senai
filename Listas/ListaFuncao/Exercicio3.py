def converter_celsius_para_fahrenheit(celsius):
    fah = (celsius * 1.8) + 32
    return fah

celsius = float(input("Insira o valor em Cº: "))
resultado = converter_celsius_para_fahrenheit(celsius)

print(f"A conversão foi: de {celsius:.1f}Cº para {resultado:.1f}F")