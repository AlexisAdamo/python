#Crea un vector de 10 elementos con valores aleatorios entre 1 y 100.
import random
#random > biblioteca que permite generar numeros aleatorios
print("Este es un vector de 10 elementos con numeros del 1 al 100")
vector = [random.randint(1,100) for i in range(10)]
'''
random.randit(1,100) > genera un numero aleatorio para cada elemento de vector 
'''
print(vector)

