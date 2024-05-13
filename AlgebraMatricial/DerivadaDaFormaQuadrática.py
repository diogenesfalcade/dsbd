import numpy as np

# Definição das matrizes I e Z
I = np.array([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
])

Z = np.array([
    [1, 1, 0, 0],
    [1, 1, 0, 0],
    [0, 0, 1, 1],
    [0, 0, 1, 1]
])

# Parâmetros τ0 e τ1
tau0 = 2
tau1 = 1

# Calculando a matriz A = τ0*I + τ1*Z
A = tau0 * I + tau1 * Z

# Vetor x
x = np.array([1, 2, 3, 4])

# Calculando a derivada de y = x^T A x em relação a x
derivada_y = 2 * np.dot(A, x)

# Avaliando a derivada no ponto x = (1, 2, 3, 4)
resultado_derivada = derivada_y

# Somando todos os valores da matriz resultado
soma_resultado = np.sum(resultado_derivada)

# Imprimindo o resultado formatado com três casas decimais
print(f'O resultado da soma dos valores da matriz resultante é: {soma_resultado:.3f}')
