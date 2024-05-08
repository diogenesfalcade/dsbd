# Considere as matrizes A e B conforme abaixo:

# A
# ##      [,1] [,2] [,3] [,4] [,5]
# ## [1,]    8   10   13   11    9
# ## [2,]   10    7    8   11    8
# ## [3,]    7   14   14   11   12
# ## [4,]    8    4   12    6    4
# ## [5,]   12    8    8   16    6
# B
# ##      [,1] [,2] [,3] [,4] [,5]
# ## [1,]    8   10   12   10   12
# ## [2,]   13    5    8    7    8
# ## [3,]   13    9   16   12    7
# ## [4,]   11    7   11   10   11
# ## [5,]   10    3    8   11   16
# Calcule a matriz o produto entre as matrizes A e B
# Coloque o resultado em uma nova matriz chamada de C
# Para incluir a sua resposta some todos os elementos da matriz C
# Sua resposta deve ser um único número. Use três casas decimais (se necessário).


import numpy as np

# Define the matrices A and B
A = np.array([[8, 10, 13, 11, 9],
              [10, 7, 8, 11, 8],
              [7, 14, 14, 11, 12],
              [8, 4, 12, 6, 4],
              [12, 8, 8, 16, 6]])

B = np.array([[8, 10, 12, 10, 12],
              [13, 5, 8, 7, 8],
              [13, 9, 16, 12, 7],
              [11, 7, 11, 10, 11],
              [10, 3, 8, 11, 16]])

# Calculate the product of matrices A and B and store it in C
C = np.matmul(A, B)

# Sum all elements of matrix C
sum_of_elements = np.sum(C)

# Print the sum of elements with three decimal places
print(f"The sum of all elements in matrix C is: {sum_of_elements:.3f}")
