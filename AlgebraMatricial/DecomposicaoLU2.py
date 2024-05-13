# Considere a decomposição LU da matrix A dada abaixo. O traço da matriz U é? Sua resposta deve ser um número. Use três casas decimais (se necessário).

# A
# ##     1   2   3   4
# ## 1 1.0 0.9 0.9 0.8
# ## 2 0.9 1.0 0.8 0.9
# ## 3 0.9 0.8 1.0 0.9
# ## 4 0.8 0.9 0.9 1.0

import numpy as np
import scipy

# Definindo a matriz A
A = np.array([
    [1.0, 0.9, 0.9, 0.8],
    [0.9, 1.0, 0.8, 0.9],
    [0.9, 0.8, 1.0, 0.9],
    [0.8, 0.9, 0.9, 1.0]
])

# Definição da matriz A
A = np.array([
    [1.0, 0.7, 0.7, 0.7],
    [0.7, 1.0, 0.7, 0.7],
    [0.7, 0.7, 1.0, 0.7],
    [0.7, 0.7, 0.7, 1.0]
])

# Realizando a decomposição LU usando scipy
P, L, U = scipy.linalg.lu(A)

# Calculando o traço da matriz U
trace_U = np.trace(U)

# Imprimindo o traço de U com três casas decimais
print(f'O traço da matriz U é: {trace_U:.3f}')
