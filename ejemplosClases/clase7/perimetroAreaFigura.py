#seleccionar entre un circulo y un cuadrado. y calcular el perimetro y el area de cada figura.



def calcularCuadrado(base,altura):
    perimetro = 2 * (base+altura)
    area = (base*altura)
    return perimetro,area
    
    
def calcularCirculo(radio):
    perimetro = 2 * 3.1415 * radio
    area = 3.1415 * (radio**2)
    return perimetro, area


def calcularFigura(figura, base=None, altura=None): #None en caso de que no exista no lo usa.
    if figura.lower() == "cuadrado": #toma el valor si se igresa en mayuscula
        try :
            perimetro, area = calcularCuadrado(base,altura)
            return {"figura": "cuadrado", "perimetro": perimetro, "area": area}#reotrna dictionario
            #return calcularCuadrado(base,altura)
        except:
            raise Exception ("Se necesita una base y una altura")
    elif figura.lower() =="circulo":
        try:
            perimetro, area = calcularCirculo(base)
            return {"figura": "circulo", "perimetro": perimetro, "area": area}
        except:
            raise Exception ("Se necesita un radio")
    else:
        raise Exception ("seleccionar cuadrado o circulo")

resultado_cuadrado = calcularFigura("cuadrado", 5,6)
resultado_circulo = calcularFigura("circulo", 3)

print(resultado_cuadrado)
print(resultado_circulo)
