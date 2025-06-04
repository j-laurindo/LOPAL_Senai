print("--- SIMULAÇÃO DE POPULAÇÃO DE COELHOS ---")

coelhos_iniciais = int(input("Digite o número inicial de coelhos: "))
taxa_reproducao = float(input("Digite a taxa de reprodução (% por geração): "))
taxa_mortalidade = float(input("Digite a taxa de mortalidade (% por geração): "))
geracoes = int(input("Digite o número de gerações para simular: "))
populacao = coelhos_iniciais

for gen in range(1, geracoes + 1):
    nascimentos = populacao * (taxa_reproducao / 100)
    mortes = populacao * (taxa_mortalidade / 100)
    populacao = populacao + nascimentos - mortes
print(f"-> Na {gen}ª geração, terá uma população de: {populacao:.0f} coelhos")