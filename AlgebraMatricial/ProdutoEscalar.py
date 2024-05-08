# Considere o vetor a e o escalar alpha:

# a
# ## [1] 10 11 16 14  9
# alpha
# ## [1] 16
# Calcule a multiplicação de b=αa
# . Para incluir sua resposta faça a soma de b
# . A resposta deve ser um único valor numérico com até três casas decimais (se necessário).

import numpy as np

# Definir o vetor a como um array NumPy
a = np.array([10, 11, 16, 14, 9])

# Definir o escalar alpha
alpha = 16

# Calcular a multiplicação do vetor a pelo escalar alpha
b = alpha * a

# Calcular a soma dos elementos do vetor resultante b
soma_b = np.sum(b)

# Exibir o vetor resultante b e a soma de todos os seus elementos
print("Vetor b (resultado da multiplicação de alpha por a):", b)
print("Soma de todos os elementos de b:", soma_b)
