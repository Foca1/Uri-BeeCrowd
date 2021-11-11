from collections import defaultdict

for i in range(int(input())):
    palavra = input().lower().replace(" ", "")
    letras_rep = defaultdict(int)
    i, soma = 0, 0
    letras_maiores, maiores_rep = [], []

    for letra in palavra:
        n_rep = 0

        if letra in letras_rep:
            n_rep += 1
        letras_rep[letra] += n_rep

    for i in letras_rep:
        maiores_rep.append(letras_rep[i])

    for i in letras_rep:
        if max(maiores_rep) == letras_rep[i]:
            letras_maiores.append(i)

    for i in sorted(letras_maiores):
        print(i, end="")

    print()