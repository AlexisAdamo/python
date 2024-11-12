''''
En el siguiente codigo hay 3 errores que hay que corregir, 

un error logico > solved 
un error de tipeo > solved
un error de tipo de dato. > Esto no sucede?
Se recibe una lista de numeros y se deben devolver dos listas, una lista con los numero pares y otra con los numeros
impares.

'''


def separar_ordenar_pares_impares(lista):
    # Ordenar la lista en orden ascendente
    lista_ordenada = sorted(lista)
    print("Lista ordenada:", lista_ordenada)
    # Separar en números pares e impares
    pares = [num for num in lista_ordenada if num % 2 == 0]
    impares = [num for num in lista_ordenada if num % 2 != 0]#error logico cambio de operador logico / por %.
    # Ordenar ambas listas en orden descendente
    pares_desc = sorted(pares, reverse=True)
    impares_desc = sorted(impares, reverse=True)#correccion de inpares por impares.
    print("Números pares en orden descendente:", pares_desc)
    print("Números impares en orden descendente:", impares_desc)
# Prueba
lista = [5, 3, 8, 6, 7, 2]#Error de dato: () usa una tupla, [] las listas
separar_ordenar_pares_impares(lista)