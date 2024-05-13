import numpy as np

# Definição da matriz A
A = np.array([
    [7, 14, 6, 18, 8],
    [4, 10, 12, 8, 9],
    [11, 5, 11, 8, 13],
    [13, 4, 18, 9, 9],
    [8, 9, 8, 10, 7]
])

# Calculando o determinante de A
determinante_A = np.linalg.det(A)

# Calculando o traço de A
traco_A = np.trace(A)

# Imprimindo o determinante e o traço com até três casas decimais
print(f"O determinante de A é: {determinante_A:.3f}")
print(f"O traço de A é: {traco_A:.3f}")
