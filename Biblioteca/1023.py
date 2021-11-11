from collections import defaultdict
from math import floor
from sys import stdin

def truncate(f):                #Uri so aceita assim, por algum motivo
    return floor(f * 100) / 100

rep = int(stdin.readline())
cid = 1

while True:
    if rep==0:
        break

    mor_cons = defaultdict(int)         #Cria um dicionario de inteiro 
    soma_cons, soma_mor = 0, 0

    for i in range(rep):    
        n_morador, cons_total = map(int, stdin.readline().split())

        mor_cons[cons_total//n_morador] += n_morador    #As chaves são as medias, e o valor a quantidade de morador

        soma_cons += cons_total
        soma_mor += n_morador   
    
    print(f"Cidade# {cid}:")
    print(' '.join(f'{mor_cons[i]}-{i}' for i in sorted(mor_cons)))     
    print(f"Consumo medio: {truncate(soma_cons/soma_mor):.2f} m3.")
    cid+=1

    rep = int(input()) #Input do numero de predios a seguir 
    print()