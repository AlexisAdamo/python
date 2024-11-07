#manejo de archivos


#with open('Archivo.txt','r') as archivo:
#    contenido = archivo.read()
    
#print(contenido)

with open('python\ejemplos clases\clase 5\Archivo.txt','r', encoding='utf-8') as archivo:#abre y repara el archivo
    contenido = archivo.read()
print(contenido)

print("\n  ----------------------------\n")

with open('python\ejemplos clases\clase 5\Archivo.txt','r', encoding='utf-8') as archivo:#abre y repara el archivo
    contenido = archivo.readlines()
print(contenido)

print("\n  ----------------------------\n")

contenido[2] = "mister bombastic, mister fantastic \n"

with open('python\ejemplos clases\clase 5\Archivo.txt','w', encoding='utf-8') as archivo:
    archivo.writelines(contenido)
    
    
print("\n  ----------------------------\n")

with open('python\ejemplos clases\clase 5\Archivo.txt','a', encoding='utf-8') as archivo:# a = append
    archivo.writelines("\nHola a todos, yo soy el LEON")
    
print("\n  ----------------------------\n")

with open('python\ejemplos clases\clase 5\Milei.txt','x', encoding='utf-8') as archivo:# x = crea archivo si el archivo no existe
    archivo.writelines("Hola a todos, yo soy el LEON") #si existe da error.