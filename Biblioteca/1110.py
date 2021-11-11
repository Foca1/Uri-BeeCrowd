def cards(nums: int):
    listNums = [i for i in range(1,nums+1)]
    discarded = []

    while len(listNums) > 1:
        discarded.append(listNums[0])
        listNums.remove(listNums[0])

        listNums.insert(len(listNums), listNums[0])
        listNums.remove(listNums[0])

    return (discarded, listNums)

while True:
    numCards = int(input())
    if numCards == 0:
        break
    
    myCards = cards(numCards)
    print(f"Discarded cards: {', '.join(str(i) for i in myCards[0])}")
    print(f"Remaining card: {myCards[1][0]}")