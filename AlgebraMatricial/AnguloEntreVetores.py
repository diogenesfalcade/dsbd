# Considere o vetores a e b:

# a
# ## [1]  8  5  8 10  8
# b
# ## [1] 14  7 16  9  8
# Calcule o ângulo θ entre a e b. Sua resposta deve ser um único número com até três casas decimais (se necessário).


import numpy as np

def angle_between_vectors(a, b):
    dot_product = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    
    cos_theta = dot_product / (norm_a * norm_b)
    
    # Tratamento para evitar erros de arredondamento que podem causar valores ligeiramente fora do intervalo [-1, 1]
    cos_theta = np.clip(cos_theta, -1.0, 1.0)
    
    theta = np.arccos(cos_theta)
    return np.degrees(theta)  # Convertendo de radianos para graus

# Vetores a e b dados
a = np.array([8, 5, 8, 10, 8])
b = np.array([14, 7, 16, 9, 8])

# Calculando o ângulo entre a e b
angle = angle_between_vectors(a, b)

# Imprimindo o ângulo com até três casas decimais
print(f"O ângulo θ entre os vetores a e b é: {angle:.3f} graus")
