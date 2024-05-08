# Considere o vetores a e b :

# a
# ## [1]  9  6  7  9 13
# b
# ## [1]  8  7 17  4 13
# Calcule o produto de Hadamard de a por b , 
# ou seja c=a⨀b. Para incluir sua resposta faça a soma de c. 
# A resposta deve ser um único valor numérico com até três casas decimais (se necessário).

import numpy as np

# Definir os vetores a e b como arrays NumPy
a = np.array([9, 6, 7, 9, 13])
b = np.array([8, 7, 17, 4, 13])

# Calcular o produto de Hadamard (element-wise) de a por b
c = a * b

# Calcular a soma do vetor resultante c
soma_c = np.sum(c)

# Exibir o vetor resultante c e a soma de c
print("Vetor resultante (c):", c)
print("Soma do vetor resultante (c):", soma_c)
