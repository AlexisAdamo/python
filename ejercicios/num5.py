#imprimir una candena de texto con los puntos entre sus letras
palabra = (input("Ingrese una palabra: "))
separador = ".".join(list(palabra))#list convierte en lista de caracteres, join los une con el simbolo "." 
print(separador)


""""
resuelto de manera mas simple
palabra = (input("Ingrese una palabra: "))
print(".".join(palabra))


"""