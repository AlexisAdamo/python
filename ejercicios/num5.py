#imprimir una candena de texto con los puntos entre sus letras
palabra = int(input("Ingrese una palabra: "))
separador = ".".join(list(palabra))#list combierte en lista de caracteres, join los une con el simbolo "." 
print(separador)

