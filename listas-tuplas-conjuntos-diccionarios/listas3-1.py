#Crea una lista con al menos 5 palabras.v
#Ordena la lista en orden alfabético inverso (Z a A) y muestra la lista ordenada.


listaPalabras = ["zorro", "linterna", "arbol", "tornado", "arroz" ]

print(f"Lista Orginal:\n", listaPalabras)
listaPalabras.sort()
print("Lista ordenada alfabeticamente: \n",listaPalabras)

listaPalabras.reverse()
print(f"Lista ordenada alfabeticamente inversa: \n", listaPalabras)