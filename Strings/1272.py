def primeira(lista: list, p_final: str = ""):
    for i in lista:
        p_final += i[0]

    return p_final

if __name__ == "__main__":
    for i in range(int(input())):
        palavra = input().split()
        print(primeira(palavra))