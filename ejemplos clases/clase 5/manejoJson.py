import json
with open('python\ejemplos clases\clase 5\Archivo.json','r') as iteraciones:
    datos = json.load(iteraciones) #carga el json
    
print(datos)

datos["profecion"]="ingeniero"