def calcular_troco(valor_compra, valor_pago):
    if valor_pago > valor_compra:
        troco = valor_pago - valor_compra
        print(f"-> TROCO DA COMPRA: R${troco:.2f}")
    elif valor_pago == valor_compra:
        print("-> PAGAMENTO SUFICIENTE! Não é necessário dar o troco.")
    else:
        faltante = valor_compra - valor_pago
        print(f"-> PAGAMENTO INSUFICIENTE! Ainda faltou R${faltante:.2f} a serem pagos.")

valor_compra = float(input("Digite o valor total da compra: R$"))
valor_pago = float(input("Digite o valor pago pelo cliente: R$"))

calcular_troco(valor_compra,valor_pago)
