tentativa = 1

print("--- ENTRE NO NOSSO SISTEMA ---")
while tentativa <= 3:
    senha = input("\nDigite sua senha: ")
    senha_correta = "123py"
    if senha == senha_correta:
        break
    else:
        tentativa += 1
if tentativa > 3:
    print("\n-> ACESSO BLOQUEADO")
else:
    print("\n-> ACESSO PERMITIDO")