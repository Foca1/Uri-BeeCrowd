for i in range(int(input())):
    palavra = input()
    des = int(input()) #Quantos vai deslocar
    nova = ''

    for i in palavra:
        if ord(i)-des < 65:                    #Se for menor que o valor das letras na tabelas ASCII
            nova += chr(91-(65-(ord(i)-des)))  #A letra deslocada vai ser subtraida do valor da letra A, e depois subtraida do valor da letra Z
        else:                                  #Letra B desloca 3, B-3 = ?(63), 65 - ?(63) = stx(2), 91 - stx = Y(89)
            nova += chr(ord(i)-des)

    print(nova)
