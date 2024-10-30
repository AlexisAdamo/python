#Escribir un programa que realice la convercion de grados celius a fahrenheit. 

#funcion
def Convercion(temperatura):
    try: #en caso de que temperatura sea numerico
        return float(temperatura * (9/5)) + 32 #operacion de convercion
    except: #sino es numero retornar excepcion
        raise Exception ("La temperatura debe ser un numero")
print(Convercion(20.1))
    