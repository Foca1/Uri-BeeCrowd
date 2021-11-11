rep = int(input())

for cont in range(rep):
    val = input().split()
    x,y = val

    x,y = int(x),int(y)
    soma,i = 0,1

    while(i<=y):
        if(x%2!=0):
            soma+=x
            x+=1
            i+=1
        else:
            x+=1
    print(soma)