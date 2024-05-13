import numpy as np

np.set_printoptions(precision=6)

def gauss_seidel(A, b, x0, tol=1e-4, max_iter=1000):
    n = len(b)
    x = np.copy(x0)
    x_new = np.zeros_like(x)
    iters = 0
    converged = False
    
    while iters < max_iter:
        for i in range(n):
            sum1 = np.dot(A[i, :i], x_new[:i])
            sum2 = np.dot(A[i, i+1:], x[i+1:])
            x_new[i] = (b[i] - sum1 - sum2) / A[i, i]
        
        if np.linalg.norm(x_new - x) < tol:
            converged = True
            break
        
        x[:] = x_new
        iters += 1
    
    if converged:
        return x, iters
    else:
        raise ValueError("Gauss-Seidel did not converge within the maximum number of iterations.")

# Definir a matriz A e o vetor b
A = np.array([
    [2.5, 0.8, 0.8, 0.7],
    [0.8, 2.5, 0.7, 0.8],
    [0.8, 0.7, 2.5, 0.8],
    [0.7, 0.8, 0.8, 2.5]
])

b = np.array([12, 11, 15, 11])

# Vetor inicial de zeros
x0 = np.zeros_like(b)

# Resolver o sistema usando o método de Gauss-Seidel
solution, num_iterations = gauss_seidel(A, b, x0)

# Imprimir a solução e o número de iterações
print("Solução encontrada pelo Gauss-Seidel:", solution)
print("Número de iterações necessárias para convergir:", num_iterations)
