# Considere o escalar α e a matriz A conforme abaixo:

# A
# ##      [,1] [,2] [,3] [,4] [,5]
# ## [1,]   10   12    6   11   16
# ## [2,]   11    7   10    5   11
# ## [3,]   11    0    7   10   14
# ## [4,]   13   13    8   13   10
# ## [5,]    8    8   10   10   11
# alpha
# ## [1] 3
# Calcule a matriz C=αA
# Para incluir a sua resposta some todos os elementos da matriz C
# Sua resposta deve ser um único número. Use três casas decimais (se necessário).

import numpy as np

# Definir a matriz A
A = np.array([
    [10, 12,  6, 11, 16],
    [11,  7, 10,  5, 11],
    [11,  0,  7, 10, 14],
    [13, 13,  8, 13, 10],
    [ 8,  8, 10, 10, 11]
])

# Definir o escalar alpha
alpha = 3

# Calcular a matriz C = alpha * A
C = alpha * A

# Calcular a soma de todos os elementos em C
soma_elementos_C = np.sum(C)

# Imprimir a soma com três casas decimais
print(f'{soma_elementos_C:.3f}')
