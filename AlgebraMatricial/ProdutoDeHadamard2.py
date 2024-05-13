# Considere o vetores a  e b:

# a
# ## [1]  8 11 15  5 10
# b
# ## [1]  9  8 12 15  9
# Calcule o produto de Hadamard de a  por b, ou seja c=a⨀b. 
# Para incluir sua resposta faça a soma de c. A resposta deve ser um único valor numérico com até três casas decimais (se necessário).

import numpy as np

# Definir os vetores a e b
a = np.array([8, 11, 15, 5, 10])
b = np.array([9, 8, 12, 15, 9])

# Calcular o produto de Hadamard entre a e b
c = a * b

# Calcular a soma dos elementos de c
soma_c = np.sum(c)

# Imprimir o resultado formatado com até três casas decimais
print(f'A soma do produto de Hadamard entre a e b é: {soma_c:.3f}')
