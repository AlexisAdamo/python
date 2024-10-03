#Crea una lista con x números aleatoreos del del 1 al 100.
#y suma los valores

import numpy as np
import random

x = 15 # defino el tamaño de la lista

# listaRandom = [random.sample(1,100) for i in range (x)] 
#ramdom.sample genera numeros que no se repitan

#creo una lista de de numeros random en un for del tamaño pre definido
listaRandom = [random.randint(1,100) for i in range (x)]
#random.randint genera numero que se pueden repetir.

print(f"Esta es una lista de 5 de tamaño que contiene numeros random: ",listaRandom)

print(f"Esta es la suma de los valores de la lista random:", np.sum(listaRandom))
# np.sum suma los valores de la variable

