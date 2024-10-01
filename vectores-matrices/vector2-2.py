# Suma ambas matrices e imprime el resultado.
import numpy as np

matriz1 = np.random.randint(1,11,(3,3))# random.randint = numeros enteros random.
matriz2 = np.random.randint(1,11,(3,3))

ope = matriz1+matriz2



print("matriz 1: ")
print(matriz1)
print("matriz 2: ")
print(matriz2)


print("esta es la suma de las matrices 1 y 2:")
print(ope)