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
        if nombreCancion is None or artista is None:
            raise Exception ('Algun valor es incorrecto:\n nombre de cancion y artista No pueden estar vacios')
        self.nombreCancion = nombreCancion
        self.artista = artista
        self.generoMusical=generoMusical
        self.duracion=duracion
        self.anioEdicion=anioEdicion
        self.numeroLikes=NumeroLikes
    
          
          
    def __str__(self):
        return f'Nombre Cancion: {self.nombreCancion}, Artista: {self.artista}, Genero Musical: {self.generoMusical}, Duracion: {self.duracion}, Año Edicion: {self.anioEdicion}, Numero de Likes: {self.numeroLikes}'
        
cancion_1=Cancion(2.33, 2005, 55000)
print(cancion_1)