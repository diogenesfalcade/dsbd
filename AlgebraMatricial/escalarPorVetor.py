# Considere o vetor a e o escalar alpha:

# a
# ## [1]  7  8 12  9  6
# alpha
# ## [1] 11
# Calcule a multiplicação de b=αa
# . Para incluir sua resposta faça a soma de b
# . A resposta deve ser um único valor numérico com até três casas decimais (se necessário).

import numpy as np

# Definir o vetor a e o escalar alpha
a = np.array([7, 8, 12, 9, 6])
alpha = 11

# Calcular a multiplicação de b = alpha * a
b = alpha * a

# Calcular a soma dos elementos de b
soma_b = np.sum(b)

# Imprimir o resultado formatado com até três casas decimais
print(f'A soma da multiplicação de b por alpha é: {soma_b:.3f}')
