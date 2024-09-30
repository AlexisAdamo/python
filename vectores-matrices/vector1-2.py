#Cambia el valor del quinto elemento del vector por 0.
import numpy as np
#import random
#random > biblioteca que permite generar numeros aleatorios
print("Este es un vector de 10 elementos con numeros del 1 al 100")
vector = [np.random.randint(1,100) for i in range(9)]
'''
random.randit(1,100) > genera un numero aleatorio para cada elemento de vector 
'''
vector2 = (vector.insert(4,0))
print(vector)
#print(vector2)


