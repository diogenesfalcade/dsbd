# Obtenha os valores singulares da matriz A
# 𝐴 abaixo. Sua resposta deve ser quatro valores. Use três casas decimais (se necessário).
# A
# ##      [,1] [,2] [,3] [,4] [,5]
# ## [1,]   10   10   12   10   16
# ## [2,]    9    8    9   11    9
# ## [3,]   14    8    7   10    3
# ## [4,]    7    7    7   10   10


import numpy as np

# Define the matrix A
A = np.array([[10, 10, 12, 10, 16],
              [9, 8, 9, 11, 9],
              [14, 8, 7, 10, 3],
              [7, 7, 7, 10, 10]])

# Calculate the singular values of matrix A and round to 3 decimal places
singular_values = np.linalg.svd(A, compute_uv=False)
singular_values = np.round(singular_values, decimals=3)

# Print the singular values
print("The singular values of matrix A are:")
for value in singular_values:
  print(value)
