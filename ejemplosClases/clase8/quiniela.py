# primer numero, seugndo numero  y un multiplicador
# funcion ganador si numero es == numero randit ganamos premio
# importe a pagar: se toma apuestay  se multiplica por apuesta retorna el precio
# si sale segundo, se divide en 2 
import random
class Quiniela:
    def __init__ (self, primer_numero, segundo_numero, apuesta):
        if primer_numero < 0 or segundo_numero < 0 or apuesta < 1:
            raise Exception ("los numeros no puedes ser negativos y la apuesta no puede ser 0")
        elif primer_numero == segundo_numero:
            raise Exception("No se puede seleccionar dos veces el mismo numero")
        self.primer_numero = primer_numero
        self.segundo_numero = segundo_numero
        self.apuesta = apuesta
        self.numero_ganador = random.randint(0,5)
    
    def __str__ (self):
        return f'Primer Numero seleccionado: {self.primer_numero}\nSegundo Numero seleccionado: {self.segundo_numero}\nApuesta Total: {self.apuesta}'
        
        
    def ganadorQuiniela(self):
        if self.primer_numero == self.numero_ganador:
            premio = "primer Premio"
        elif self.segundo_numero == self.numero_ganador:
            premio = "segundo Premio"
        else: 
            premio = "Segui Participando"
        return premio
        
    def gananciaDeApuesta(self):
        if self.primer_numero == self.numero_ganador:
            print(f"Usted acerto el primer premio y gano: {self.apuesta*50}") 
        elif self.segundo_numero == self.numero_ganador:
            print(f"Usted acerto el primer premio y gano: {self.apuesta*25}")
        elif self.primer_numero != self.numero_ganador and self.segundo_numero != self.numero_ganador:
            print("No hubo Ganancia") 


      


quiniela_1 = Quiniela(2,3,5)
print(quiniela_1)
print(f"Numero Ganador: {quiniela_1.numero_ganador}")
print(quiniela_1.gananciaDeApuesta())