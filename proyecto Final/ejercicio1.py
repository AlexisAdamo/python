''''
Implementar el TDA "Cancion" con los siguientes componentes:
Nombre
Artista
Duración
Género musical (6 posibles: Rock, Jazz, Blues, Funk, Reggae y Rap).
Año de edición
Número de likes
Implementar las siguientes operaciones:
Constructor: Debe incluir las validaciones necesarias.
str: Al usar la función print con una variable del tipo canción debe mostrar: 'nombre' - 'artista' ('duracion').
mayorDuracion: Operación que recibe dos canciones por parámetros y retorna la de mayor duración.
agregaLikes: Operación que recibe un número e incrementa la cantidad de likes de la canción en ese número.
masVotada: Operacion que recibe dos canciones y sin son del mismo artista y del mismo género musical, retorna
la que tiene mayor cantidad de likes. En caso contrario debe lanzar una excepción.
'''

class Cancion:


    def __init__ (self, nombreCancion='', artista='', generoMusical='',duracion=0, anioEdicion=0, NumeroLikes=0):
        #if generoMusical != generosPermitidos():
        #    raise Exception ('Algun valor es incorrecto:\n nombre de cancion y artista No pueden estar vacios')
        self.nombreCancion = nombreCancion
        self.artista = artista
        self.generoMusical=generoMusical
        self.duracion=duracion
        self.anioEdicion=anioEdicion
        self.numeroLikes=NumeroLikes
    
    def generosPermitidos():
        ["Rock","Jazz", "Blues", "Funk", "Reggae", "Rap"]
          
          
    def __str__(self):
        #return f'Nombre Cancion: {self.nombreCancion}, Artista: {self.artista}, Genero Musical: {self.generoMusical}, Duracion: {self.duracion}, Año Edicion: {self.anioEdicion}, Numero de Likes: {self.numeroLikes}'
        return (f"{self.nombreCancion} - {self.artista} {self.duracion}")
        
    def mayorDuracion(cancion_1, cancion_2):
        if cancion_1.duracion > cancion_2.duracion:
            print(f'La cancion: {cancion_1.nombreCancion} es la de mayor duracion: {cancion_1.duracion}')
        elif cancion_1.duracion < cancion_2.duracion:
            print(f'La cancion: {cancion_2.nombreCancion} es la de mayor duracion: {cancion_2.duracion}')
        else:
            print (f"Ambas canciones tienen la misma duracion: {cancion_1.nombreCancion} - {cancion_1.duracion} = {cancion_2.nombreCancion} - {cancion_2.duracion}")
            
    '''def agregarLikes(cancion_1,likes):
        for i in cancion_1.numeroLikes:
            cancion_1.numeroLikes + likes
            print(f"La cancion {cancion_1.nombreCancion} tiene ahora {cancion_1.numeroLikes} likes")
    '''
            
    def masVotada(cancion_1, cancion_2):
        if cancion_1.artista != cancion_2.artista:
            raise Exception ('Solo se puede evaluar canciones de un mismo Artista')
        else:
            if cancion_1.artista == cancion_2.artista and cancion_1.generoMusical == cancion_2.generoMusical:
                cancionMasVotada = (max(cancion_1.numeroLikes, cancion_2.numeroLikes))
                if cancionMasVotada == cancion_1.numeroLikes:
                    print(f'la cancion mas votada es: {cancion_1.nombreCancion} - {cancion_1.numeroLikes}')
                else:
                    if cancionMasVotada == cancion_2:
                        print(f'la cancion mas votada es: {cancion_2.nombreCancion} - {cancion_2.numeroLikes}')
            
    
        
cancion_1=Cancion("JIJIJI",'Patricio Rey',"Rock",2.34, 2005, 75000)
cancion_2=Cancion('Gualicho','Patricio Rey',"Rock",2.33, 2005, 105000) 
print(cancion_1)
print(cancion_2)
print(Cancion.mayorDuracion(cancion_1,cancion_2))
print(Cancion.masVotada(cancion_1,cancion_2))
#print(Cancion.agregarLikes(cancion_1,1000))