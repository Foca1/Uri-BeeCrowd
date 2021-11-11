def fatorial(valor):
    if valor == 1 or valor == 0:
        return 1
    return valor * fatorial(valor-1)

if __name__ == "__main__":
    while True:
        try:
            valor1, valor2 = map(int, input().split())
            print(fatorial(valor1) + fatorial(valor2))
        except EOFError:
            break   