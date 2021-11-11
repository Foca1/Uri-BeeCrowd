while True:
    troca,num = input().split()
    
    if(num=='0' and troca=='0'): break

    num = int(num.replace(troca,""))
    print(num)