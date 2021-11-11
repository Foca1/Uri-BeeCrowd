soma_idade = 0
len_id = 0

while True:
    idades = int(input())
    if(idades<0):
        print(f"{soma_idade/(len_id):.2f}")
        break
    soma_idade+=idades
    len_id+=1