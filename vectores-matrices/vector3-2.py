# Crea una matriz de 4x4 con valores aleatorios entre 1 y 50.
#Reemplaza los valores pares de la matriz por 0.
import numpy as np

matriz = np.random.randint(1,51,(4,4))
print(f"matriz original'\n", matriz)

matriz[matriz %2 == 0] = 0
print(f"matriz modificada\n", matriz)   
