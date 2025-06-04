import requests
def cotacao_dolar():
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL"
    try:
        resposta = requests.get(url)
        dados_moeda = resposta.json()
        cotacao = float(dados_moeda['USDBRL']['bid'])
        return cotacao
    except Exception as e:
        print("ERRO AO BUSCAR A COTAÇÃO:", e)

def conversao_reais():
    reais = cotacao_dolar()
    dolar = salario_hora

    salario_reais = dolar * reais

    salario_total = salario_reais * horas
    return salario_total

##################################################################

print("--- CALCULO DE AUMENTO DE SALÁRIO   ---")
print("""| Calcule em até quantos % seu |
|    salário foi aumentado!    |""")

nome = input("\nDigite o nome do funcionário(a): ")
anos = int(input("Digite a quantidade de tempo de casa (em anos): "))
salario_hora = float(input("Digite o quanto ele(a) recebe por hora (em dólar): "))
horas = int(input("Digite a quantidade de horas trabalhadas: "))

if anos <= 5:
    salario_real = conversao_reais()
    salario = salario_hora * horas
    print(f"\nFUNCIONÁRIO:       |  {nome}")
    print(f"SALÁRIO EM REAIS:  |  R${salario_real:.2f}")
    print(f"SALÁRIO EM DÓLAR:  |  U${salario:.2f}")
elif anos <= 15:
    salario_real = conversao_reais()
    salario = salario_hora * horas
    aumento_reais = (salario_real * (10/100)) + salario_real
    aumento_dolar = (salario * (10/100)) + salario

    print("\n------ Houve um aumento de 10% no seu salário! ------")
    print(f"FUNCIONÁRIO:       |  {nome}")
    print(f"SALÁRIO EM REAIS:  |  R${aumento_reais:.2f}")
    print(f"SALÁRIO EM DÓLAR:  |  U${aumento_dolar:.2f}")
elif anos <= 25:
    salario_real = conversao_reais()
    salario = salario_hora * horas
    aumento_reais = (salario_real * (10 / 100)) + salario_real
    aumento_dolar = (salario * (10 / 100)) + salario

    print("\n------ Houve um aumento de 20% no seu salário! ------")
    print(f"FUNCIONÁRIO:       |  {nome}")
    print(f"SALÁRIO EM REAIS:  |  R${aumento_reais:.2f}")
    print(f"SALÁRIO EM DÓLAR:  |  U${aumento_dolar:.2f}")