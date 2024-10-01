# resta la segunda a la primera e imprmir el resultado
import numpy as np

matriz1 = np.random.randint(1,11,(3,3))# random.randint = numeros enteros random.
matriz2 = np.random.randint(1,11,(3,3))

ope = matriz2 - matriz1



print("matriz 1: ")
print(matriz1)
print("matriz 2: ")
print(matriz2)


print("esta es la resta de las matrices 2 y 1:")
print(ope)