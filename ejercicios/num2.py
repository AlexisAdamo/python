#imprimir la tabla del 5
multiplicador = 5

print(f"Esta es la tabla del {multiplicador}")
for ini in range(1,11):
    operacion =  ( ini * multiplicador)
    print(f"{multiplicador} * {ini} = {operacion}")