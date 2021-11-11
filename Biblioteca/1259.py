while True:
  try:
    qtNumeros = int(input())
    pares, impares, numeros = [],[],[]

    for i in range(qtNumeros):
      numeros.append(int(input()))

    for numero in numeros:
      if numero%2 == 0:
        pares.append(numero)
      else:
        impares.append(numero)

    pares = sorted(pares, key=int)
    impares = sorted(impares, key=int, reverse=True)

    for par in pares:
      print(par)
    for impar in impares:
      print(impar)
  except EOFError:
    break