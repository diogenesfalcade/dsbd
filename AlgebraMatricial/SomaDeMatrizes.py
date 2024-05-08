# Considere as matrizes A
#  e B
#  conforme abaixo:

# A
# ##      [,1] [,2] [,3] [,4] [,5]
# ## [1,]    8   12   13   14   15
# ## [2,]    7    5   11    9    9
# ## [3,]   11    9    6    9    9
# ## [4,]   15   11    8   10   10
# ## [5,]    8   10    8   13   14
# B
# ##      [,1] [,2] [,3] [,4] [,5]
# ## [1,]   14   11   12   11   10
# ## [2,]   13   11   10    3    9
# ## [3,]    9    7    9   12   11
# ## [4,]    9   12   14    9    9
# ## [5,]    6    6    6   15   16
# Calcule a matriz C=A+B
# . Para incluir a sua resposta some todos os elementos da matriz C
# . Sua resposta deve ser um único número. Use três casas decimais (se necessário).


import numpy as np

# Definir as matrizes A e B como arrays NumPy
A = np.array([
    [8, 12, 13, 14, 15],
    [7, 5, 11, 9, 9],
    [11, 9, 6, 9, 9],
    [15, 11, 8, 10, 10],
    [8, 10, 8, 13, 14]
])

B = np.array([
    [14, 11, 12, 11, 10],
    [13, 11, 10, 3, 9],
    [9, 7, 9, 12, 11],
    [9, 12, 14, 9, 9],
    [6, 6, 6, 15, 16]
])

# Calcular a matriz C = A + B
C = A + B

# Calcular a soma de todos os elementos da matriz C
soma_total = np.sum(C)

# Exibir a matriz C e a soma total dos elementos
print("Matriz C:")
print(C)
print("\nSoma de todos os elementos de C:", soma_total)
