import numpy as np

def lado(matriz, valor, linha, coluna):
    return valor in matriz[linha-1:linha+2, coluna-1:coluna+2]

def linha_coluna(matriz, valor, linha, coluna):
    return valor in matriz[linha, :] or \
           valor in matriz[:, coluna]

def tudo(matriz, valor, linha, lf, coluna, cf):
    if (linha, coluna) == (lf, cf):  
        return int(0)
    if lado(matriz, valor, linha, coluna) or \
        linha_coluna(matriz, valor, linha, coluna): 
        return int(1)
    if abs(linha - lf) == abs(coluna - cf):    
        return int(1)
    else:   
        return int(2)

if __name__ == "__main__":
    while True:
        tabuleiro = np.zeros((8,8), dtype=int)
        
        lin_i, col_i, lin_f, col_f = map(int, input().split())
        if (lin_i + col_i + lin_f + col_f) == 0:    break
        lin_i, col_i, lin_f, col_f = lin_i-1, col_i-1, lin_f-1, col_f-1

        tabuleiro[lin_f][col_f] = 2

        print(tudo(tabuleiro, 2, lin_i, lin_f, col_i, col_f))