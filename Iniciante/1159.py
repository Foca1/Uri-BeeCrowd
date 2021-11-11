x = 1

while(True):
    soma = 0
    x = int(input())
    if x==0:break

    elif x%2==0:
        for i in range(x,x+10):
            if i%2==0:
                soma+=i
    else:
        for i in range(x+1,x+10):
            if i%2==0:
                soma+=i
    print(soma)