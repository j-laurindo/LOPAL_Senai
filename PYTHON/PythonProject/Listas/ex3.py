print("---- VENHA CONHECER O NOSSO MENU DE COMIDAS!!-----")

while True:
    print("\n\n---- NOSSO MENU ----")
    print("-> 1) Macarrão a Bolanhesa")
    print("-> 2) Risoto de Camarão")
    print("-> 3) Esfihas de Carne")
    print("-> 4) Lasanha ao Molho Branco")
    resposta = input("\nDigite 'sair' caso queira encerrar: ")
    opcao = resposta.lower()

    if opcao == "sair":
        break