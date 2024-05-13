# Use o método de Jacobi para resolver o sistema Ax=b onde A e b são dados abaixo. 
# Quantas iterações foram necessárias para o método convergir? Use como valores iniciais um vetor de zeros. Sua resposta deve ser apenas um número inteiro.

# A
# ##      [,1] [,2] [,3] [,4]
# ## [1,]  2.5  0.8  0.8  0.7
# ## [2,]  0.8  2.5  0.7  0.8
# ## [3,]  0.8  0.7  2.5  0.8
# ## [4,]  0.7  0.8  0.8  2.5
# b
# ## [1]  9 11  4 10

import numpy as np

def jacobi(A, b, inicial, max_iter=1000, tol=1e-4):
    n = len(b)
    x_temp = np.zeros((max_iter, n))
    x_temp[0, :] = inicial
    x = x_temp[0, :].copy()

    for j in range(1, max_iter):
        for i in range(n):
            sum_ax = np.dot(A[i, :], x) - A[i, i] * x[i]
            x_temp[j, i] = (b[i] - sum_ax) / A[i, i]

        x = x_temp[j, :]
        if np.sum(np.abs(x_temp[j, :] - x_temp[j-1, :])) < tol:
            break

    solution = x_temp[j, :]
    iterations = j + 1  # Contar iterações (começando de 1)

    return {"Solucao": solution, "Iteracoes": x_temp[:iterations, :]}

# Definição da matriz A, vetor b e valor inicial
A = np.array([
    [2.5, 0.8, 0.8, 0.7],
    [0.8, 2.5, 0.7, 0.8],
    [0.8, 0.7, 2.5, 0.8],
    [0.7, 0.8, 0.8, 2.5]
])
b = np.array([9, 11, 4, 10])
inicial = np.zeros(len(b))  # Vetor inicial de zeros

# Chamando a função jacobi para resolver o sistema
resultado = jacobi(A, b, inicial)

# Imprimindo a solução e o número de iterações necessárias
print("Solucao aproximada do sistema Ax = b:")
print(resultado["Solucao"])
print("Numero de iteracoes necessarias para convergir:", resultado["Iteracoes"].shape[0])
