# Considere uma matriz A cuja decomposição em autovalores e autovetores é dada abaixo. Obtenha o log do determinante da inversa de A.

# eigen(A)
# ## eigen() decomposition
# ## $values
# ## [1] 33  3  3  1
# ## 
# ## $vectors
# ##      [,1]          [,2]          [,3] [,4]
# ## [1,] -0.5  0.000000e+00  7.071068e-01  0.5
# ## [2,] -0.5 -7.071068e-01  3.330669e-16 -0.5
# ## [3,] -0.5  7.071068e-01 -3.885781e-16 -0.5
# ## [4,] -0.5 -8.881784e-16 -7.071068e-01  0.5

import numpy as np

# Definir os autovalores e autovetores a partir da decomposição fornecida
autovalores = np.array([33, 3, 3, 1])
autovetores = np.array([
    [-0.5,  0.000000e+00,  7.071068e-01,  0.5],
    [-0.5, -7.071068e-01,  3.330669e-16, -0.5],
    [-0.5,  7.071068e-01, -3.885781e-16, -0.5],
    [-0.5, -8.881784e-16, -7.071068e-01,  0.5]
])

# Calcular o determinante de A
det_A = np.prod(autovalores)

# Calcular o determinante da inversa de A
det_inv_A = 1 / det_A

# Calcular o log do determinante da inversa de A
log_det_inv_A = np.log(det_inv_A)

# Imprimir o resultado
print(f'O log do determinante da inversa de A é: {log_det_inv_A:.6f}')
