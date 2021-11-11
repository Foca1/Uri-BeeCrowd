rep = int(input())

for i in range(rep):
    novo = ''
    word1, word2 = input().split()

    if(len(word1) >= len(word2)):
        for i in range(len(word2)):
            novo += word1[i] + word2[i]
        #Vai pegar o tamanho da segunda palavra, e usar para cortar a palavra 1, a palavra nova vai botar as letras que nao tem correspondecia na outra.
        novo += word1[len(word2):]
    else:
        for i in range(len(word1)):
            novo += word1[i] + word2[i]
        novo += word2[len(word1):]

    print(novo)