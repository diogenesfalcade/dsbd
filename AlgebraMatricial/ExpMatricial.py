# Obtenha a exponencial matricial da matriz A
#  abaixo. Para inserir a sua resposta calcule o traço da matriz resultante.

# A
# ##     1   2   3   4
# ## 1 1.0 0.8 0.8 0.7
# ## 2 0.8 1.0 0.7 0.8
# ## 3 0.8 0.7 1.0 0.8
# ## 4 0.7 0.8 0.8 1.0

import numpy as np
from scipy.linalg import expm

# Definir a matriz A como um array NumPy
A = np.array([
    [1.0, 0.8, 0.8, 0.7],
    [0.8, 1.0, 0.7, 0.8],
    [0.8, 0.7, 1.0, 0.8],
    [0.7, 0.8, 0.8, 1.0]
])

# Definir a matriz A como um array NumPy
A = np.array([
    [1.0, 0.8, 0.8, 0.7],
    [0.8, 1.0, 0.7, 0.8],
    [0.8, 0.7, 1.0, 0.8],
    [0.7, 0.8, 0.8, 1.0]
])
# Calcular a exponencial matricial de A usando expm do SciPy
expA = expm(A)

# Calcular o traço da matriz resultante expA
traco_expA = np.trace(expA)

# Exibir a matriz resultante expA e o traço da matriz
print("Exponencial matricial de A (exp(A)):")
print(expA)
print("\nTraço da matriz exp(A):", traco_expA)

