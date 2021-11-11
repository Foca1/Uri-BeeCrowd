while True:
    try:
        word = input()
        underl, astrisk = False, False
        new_word = []
        i = 0

        for char in word:
            new_word.append(char)

            if char == "_":
                if underl == False:
                    new_word[i] = "<i>"
                    underl = True
                else:
                    new_word[i] = "</i>"
                    underl = False

            if char == "*":
                if astrisk == False:
                    new_word[i] = "<b>"
                    astrisk = True
                else:
                    new_word[i] = "</b>"
                    astrisk = False
            i += 1
        print(*new_word, sep="")
        
    except EOFError:
        break