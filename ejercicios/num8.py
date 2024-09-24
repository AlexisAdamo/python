#imprimir los numeros impares entre 1 y 20 en un bucle while
'''
num = 10
cont = 0

while True:
  print(num)
  cont +=1
  if cont == 10:
    break

'''

i = 1

print(f"Los numeros impares entre 1 y 20 son: ")
while i <= 20:
    if i % 2!= 0:
      print(f"{i}")
    i += 1