#Eliminar elementos repetidos de una lista:
import numpy as np
import random

x = 15

listaRandom = [random.randint(1,11) for i in range (x)]
print(f"Esta es un lista random de tamaño 15\n", listaRandom)

listaSinRepetidos = np.unique(listaRandom)
#np.unique funcion de numpy que devuelve los valores unicos 
print(f"Esta es la lista sin valores repetidos", listaSinRepetidos)
