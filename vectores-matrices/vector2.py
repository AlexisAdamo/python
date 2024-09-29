#Cambia el valor del quinto elemento del vector por 0.

import random
#random > biblioteca que permite generar numeros aleatorios
print("Este es un vector de 10 elementos con numeros del 1 al 100")
vector = [random.randint(1,100) for i in range(10)]
'''
random.randit(1,100) > genera un numero aleatorio para cada elemento de vector 
'''
vector2 = (vector.insert(5,0))
print(vector)
print(vector2)
