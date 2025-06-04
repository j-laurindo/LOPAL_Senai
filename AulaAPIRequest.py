import requests

def pegar_cotacao_dolar():
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
    try:
        resposta = requests.get(url)
        dados = resposta.json
        cotacao = float(dados['USDBRL']['bid'])
        return cotacao
    except Exception as e:
        print("Erro ao buscar cotação: ",e)

pegar_cotacao_dolar()