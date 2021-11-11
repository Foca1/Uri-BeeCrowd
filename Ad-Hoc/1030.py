from collections import deque

qt_rodada = 1
for i in range(int(input())):
    qt_homens, salto = map(int, input().split())

    qt_homens = deque([i for i in range(1,qt_homens+1)])

    while len(qt_homens) > 1:
        qt_homens.rotate(-salto)
        qt_homens.pop()

    print(f"Case {qt_rodada}: {qt_homens[0]}")
    qt_rodada += 1