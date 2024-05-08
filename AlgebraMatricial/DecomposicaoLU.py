# Considere a decomposição LU
#  para solução de sistemas lineares do tipo Ax=b
# A matriz A e o vetor b são dados abaixo. Considerando a notação utilizada no curso obtenha a solução intermediária y. Sua resposta deve ser um número com a soma do vetor y. Use três casas decimais (se necessário).

# A
# ##     1   2   3   4
# ## 1 1.0 0.9 0.9 0.9
# ## 2 0.9 1.0 0.9 0.9
# ## 3 0.9 0.9 1.0 0.9
# ## 4 0.9 0.9 0.9 1.0
# b
# ## [1] 12  5 15  7


import numpy as np

# Definir a matriz A e o vetor b
A = np.array([
    [1.0, 0.9, 0.9, 0.9],
    [0.9, 1.0, 0.9, 0.9],
    [0.9, 0.9, 1.0, 0.9],
    [0.9, 0.9, 0.9, 1.0]
])

b = np.array([12, 5, 15, 7])

# Obter a dimensão da matriz A
n = len(A)

# Inicializar a matriz L (matriz identidade) e U (cópia de A)
L = np.eye(n)
U = A.copy()

# Realizar a decomposição LU
for k in range(n-1):  # Iterar sobre as colunas de U
    for i in range(k+1, n):  # Iterar sobre as linhas abaixo da diagonal
        if U[i, k] != 0:
            factor = U[i, k] / U[k, k]
            L[i, k] = factor  # Armazenar o fator na matriz L
            U[i, k:] -= factor * U[k, k:]  # Atualizar os elementos da linha de U

# Resolver Ly = b (substituição progressiva)
y = np.zeros(n)
for i in range(n):
    y[i] = b[i] - np.dot(L[i, :i], y[:i])

# Resolver Ux = y (substituição regressiva)
x = np.zeros(n)
for i in range(n-1, -1, -1):
    x[i] = (y[i] - np.dot(U[i, i+1:], x[i+1:])) / U[i, i]

# Calcular a soma dos elementos de y
soma_y = np.sum(y)

# Imprimir a soma de y com três casas decimais
print(f'{soma_y:.3f}')
print(y)