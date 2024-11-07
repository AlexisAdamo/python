#archivo manejo de strigs


string1 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
string2 = """hola""" 
string3 ="""

hola
todo

""" 
string4 = '''tester'''


print(string1)
print(string2)
print(string3)
print(string4)


print(string1[6])# imprime el elemento 6 dentro del string
print(string1[6:31])# imprime los elementos del 6 al 31 dentro del string
print(string1[:31])# imprime los elementos hasta ek 31 dentro del string
print(string1[-31])# imprime los elementos del 31 al final dentro del string
print(string1[::1])# imprime la cadena

#find and index buscan en la candena


print(string1.find("dicat"))# si encuentra esto devuelve la posicion en la que se encuentra aen la cadena sino -1


print("\n  ----------------------------")

print(string1.upper())

print("\n  ----------------------------")
print(string1.lower())

print("\n  ----------------------------")
print(string1.strip("Boca"))#quita los espacios en blanco del principio y el final


print("\n  ----------------------------")

print(string1.replace("dolor","remplazo"))#remplata el primer elemento por el sgundo

#print(string1.split(' '))#divide el arreglo segune el separador establecido.

#union de listas a string
listaString = print(string1.split(' '))#separa los elementos del arreglo en base al separador establecido
print(listaString)

#print('- :D -'.join(listaString)) #join une los elemento de la lista atravez del simbolo establecido