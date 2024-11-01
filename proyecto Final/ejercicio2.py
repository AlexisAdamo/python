'''
Un número narcisista (o número de Armstrong) es un número que es igual a la suma de sus propios dígitos
elevados a la potencia del número de dígitos. 
Escribe un algoritmo que averigue si un numero dado es narcisista o
no. Por ejemplo:
153 es un número narcisista porque 1^3 + 5^3 + 3^3 = 153
'''
def numNacisista(num):
    #convierto el numero a  
    unidadNum=str(num)
    #obtengo la longitud del numero para obtener el exponente
    potencia=len(str(num))
    
    #print(unidadNum,potencia)
    # hago el calculo para obtener el numero narcisita
    suma= sum(int(digito) ** potencia for digito in unidadNum)
    print(f'El resultado de la suma es: {suma}')
    #Valido si suma y num son iguales
    if suma == num:
        print(f'el numero:, {num} es Narcisista')
    else:
        print (f'el numero:, {num} no es narcisita')


numNacisista(13)