for i in range(int(input())):
    a, b = input().split()
    a, b = int(a), int(b)

    r = 1

    while(r!=0):
        r = a%b
        a = b 
        b = r
    print(a)
