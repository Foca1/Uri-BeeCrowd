linha = []

for i in range(int(input())):
    linha.append(int(input()))

x = True
n = 0

for i in linha:
    if i == 1 and x:
        n += 1
        x = False
    elif i == 2 and not x:
        n += 1
        x = True

print(n)