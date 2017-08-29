# Recebe duas matrizes, A e B, calcula o produto de A por B e o coloca na matriz C.
#-----------------------------------------------------
def imprime_matriz(matriz):
    l = len(matriz) #linhas
    c = (len(matriz[0])) #colunas
    for i in range (l): 
        for j in range (c): 
            print (matriz[i][j], end="\t")
        print ()        

#-----------------------------------------------------
def multiplica_matriz(A, B):
    i=0
    j=0
    k=0
    lin_A=len(A)
    col_A=len(A[0])
    
    C = [] #C é a matriz de resultado da soma

    while i < lin_A: #colunas de A = linhas de B
        linha = [] #cada uma das linhas de C
        while j < lin_A:
            soma = 0
            while k < col_A:
                soma = soma + (A[i][k]) * (B[k][j])
                k = k+1
            linha.append(soma)
            k = 0
            j = j+1
        C.append(linha)
        k = 0
        j = 0
        i = i+1
    print()
    print("Matriz resultado da multiplicação de A por B:")
    i = 0
    j = 0
    for i in range (lin_A):
        for j in range (lin_A):
            print (C[i][j], end="\t")
        print ()
    
    return C
#----------------------------------------------
def main():
    A = [ [1, 2, -1], [0, 3, 2] ]
    B = [ [1, -1], [2, 0], [3, 2] ]
    print ("Matriz A:")
    imprime_matriz(A)
    print()
    print ("Matriz B:")
    imprime_matriz(B)
    multiplica_matriz(A, B)
#----------------------------------------------
main()
