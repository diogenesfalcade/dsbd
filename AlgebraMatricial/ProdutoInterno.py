# Considere o vetores a e b:

# a
# ## [1] 10 10  5 17 13
# b
# ## [1]  6 10  8  8  8
# Calcule o produto interno de a
#  por b
# , ou seja c=a⋅b
# . Para incluir sua resposta faça a soma de c
# . A resposta deve ser um único valor numérico com até três casas decimais (se necessário).

import numpy as np

# Definir os vetores a e b como arrays NumPy
a = np.array([10, 10, 5, 17, 13])
b = np.array([6, 10, 8, 8, 8])

# Calcular o produto interno de a por b
c = np.dot(a, b)

# Exibir o produto interno (c)
print("Produto interno (c):", c)

