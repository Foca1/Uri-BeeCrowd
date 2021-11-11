camisetas = {}

for i in range(int(input())):
    nome = input()
    detalhes = input()
    camisetas[nome] = detalhes #Detalhes como chave e nome como valor


print(sorted(camisetas.values))
