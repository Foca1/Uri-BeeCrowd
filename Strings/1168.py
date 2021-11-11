leds = (6,2,5,5,4,5,6,3,7,6)
       #0,1,2,3,4,5,6,7,8,9

rep = int(input())

for i in range(rep):
    num = input()       #Numero para saber a quantidade de leds
    total = 0
    for j in num:       #percorre a lista num
        total+=leds[int(j)]     #Soma de acordo com o indice da lista leds
    print(f"{total} leds")