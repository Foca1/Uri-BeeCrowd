while True:
    try:
        palavra = input()
        nova = ''

        j = 1

        for i in palavra:
            if i==' ':
                nova += ' '
            elif j==1:
                nova += i.upper()
                j-=1
            else:
                nova += i.lower()
                j+=1
        print(nova)
    except EOFError:
        break