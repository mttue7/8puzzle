import numpy as np

# Definindo o tamanho da matriz
linhas, colunas = 3, 3

# Criando uma matriz com números de 1 a 9
numeros = np.arange(1, linhas * colunas + 1)

# Embaralhando os números
np.random.shuffle(numeros)

# Redimensionando a matriz para 3x3
matriz = numeros.reshape(linhas, colunas)

# Substituindo o número 9 por 'x'
# Primeiro, cria uma matriz de strings para suportar o caractere 'x'
matriz_str = matriz.astype(str)
matriz_str[matriz_str == '9'] = 'x'

print("Matriz com 'x' substituindo o número 9:")
print(matriz_str)