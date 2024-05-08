# Considere as matrizes A e B conforme abaixo:

# A
# ##      [,1] [,2] [,3] [,4] [,5]
# ## [1,]   15   13   14    4    6
# ## [2,]   10   10   11   12    9
# ## [3,]    7    7    7   11   10
# ## [4,]   10   12    5    8   15
# ## [5,]    6   10    3    7    5
# B
# ##      [,1] [,2] [,3] [,4] [,5]
# ## [1,]    5   14   14    6    9
# ## [2,]    8   16   10   12    4
# ## [3,]   11   11   10   15    9
# ## [4,]    9   11   14   11   17
# ## [5,]   14    8    6    9   13

# Calcule a matriz o produto de Hadamard entre as matrizes A e B
# Coloque o resultado em uma nova matriz chamada de C
# Para incluir a sua resposta some todos os elementos da matriz C
# Sua resposta deve ser um único número. Use três casas decimais (se necessário).

import numpy as np

# Definir as matrizes A e B como arrays NumPy
A = np.array([
    [15, 13, 14, 4, 6],
    [10, 10, 11, 12, 9],
    [7, 7, 7, 11, 10],
    [10, 12, 5, 8, 15],
    [6, 10, 3, 7, 5]
])

B = np.array([
    [5, 14, 14, 6, 9],
    [8, 16, 10, 12, 4],
    [11, 11, 10, 15, 9],
    [9, 11, 14, 11, 17],
    [14, 8, 6, 9, 13]
])

# Calcular o produto de Hadamard entre as matrizes A e B
C = A * B

# Calcular a soma de todos os elementos da matriz C
soma_c = np.sum(C)

# Exibir a matriz C e a soma de todos os seus elementos
print("Matriz C (produto de Hadamard de A por B):")
print(C)
print("\nSoma de todos os elementos de C:", soma_c)


# Definir as matrizes A e B como arrays NumPy
A = np.array([
    [9, 7, 13, 10, 18],
    [14, 13, 19, 11, 12],
    [7, 13, 12, 7, 9],
    [10, 12, 12, 6, 11],
    [10, 8, 10, 9, 7]
])

B = np.array([
    [4, 12, 8, 10, 7],
    [15, 8, 8, 10, 5],
    [11, 9, 18, 7, 8],
    [11, 5, 6, 10, 6],
    [10, 12, 13, 6, 11]
])

# Calcular o produto de Hadamard entre as matrizes A e B
C = A * B

# Calcular a soma de todos os elementos da matriz C
soma_C = np.sum(C)

# Exibir a matriz resultante C e a soma de todos os seus elementos
print("Matriz C (produto de Hadamard de A por B):")
print(C)
print("\nSoma de todos os elementos de C:", format(soma_C, ".3f"))
