import numpy as np

def gauss_elimination_without_pivoting(A, b):
    n = len(b)
    
    # Montar a matriz estendida [A | b]
    Ab = np.column_stack((A, b))
    
    # Eliminação de Gauss sem pivotação
    for col in range(n - 1):  # Iterar sobre as colunas
        for row in range(col + 1, n):  # Iterar sobre as linhas abaixo da diagonal
            factor = Ab[row, col] / Ab[col, col]
            Ab[row, col:] -= factor * Ab[col, col:]
    
    # Resolver o sistema triangular superior resultante por substituição retroativa
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):  # Começando do último elemento
        x[i] = (Ab[i, -1] - np.dot(Ab[i, :-1], x)) / Ab[i, i]
    
    return x

# Matriz A e vetor b dados
A = np.array([
    [1.0, 0.5, 0.5, 0.4],
    [0.5, 1.0, 0.4, 0.5],
    [0.5, 0.4, 1.0, 0.5],
    [0.4, 0.5, 0.5, 1.0]
])
b = np.array([5, 8, 11, 9])

# Resolver o sistema linear usando eliminação de Gauss sem pivotação
solution = gauss_elimination_without_pivoting(A, b)

# Imprimir a solução com três casas decimais
print("A solução do sistema Ax = b é:", [round(sol, 3) for sol in solution])
