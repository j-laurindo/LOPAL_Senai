def contagem_regressiva(n):
    if n <= 0:
        print("FIM DA CONTAGEM")
    else:
        print(n)
        contagem_regressiva(n - 1)

n = int(input("Digite o valor final da contagem (ex:20): "))
contagem_regressiva(n)