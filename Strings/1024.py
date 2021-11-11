import re

rep = int(input())

for i in range(rep):
    nome_novo = ''
    nome = input()

    #Desloca os caracteres
    for i in nome:
    #Se for um letra do alfabeto, desloca 3, se nao so continua do jeito que ta
        if re.match("[a-zA-Z]", i):
            nome_novo+=chr(ord(i)+3)
        else:
            nome_novo+=i

    #Inverte a string
    nome_novo = nome_novo[::-1]

    #Divide a string em 2
    met = int(len(nome_novo)//2)
    met1 = nome_novo[0:met]
    met2 = nome_novo[met:]

    #Pega da metade pra frente e desloca pra esquerda
    met_nova = ''
    for i in met2:
        met_nova += chr(ord(i)-1)

    nome_novo = met1+met_nova
    print(nome_novo)