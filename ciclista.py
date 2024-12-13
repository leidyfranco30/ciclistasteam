class  Ciclista:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
class Velocista(Ciclista):
    def __init__(self, nombre, edad, nacionalidad, velocidad_punta):
        super(). __init__(nombre,edad,nacionalidad)
        self.velocidad_punta = velocidad_punta
        
class Montanista(Ciclista):
    def __init__(self, nombre, edad, nacionalidad,habilidad_escalar):
        super().__init__(nombre,edad,nacionalidad)
        self.habilidad_escalar =habilidad_escalar
        
class Contrarelojista(Ciclista):
    def __init__(self, nombre, edad, nacionalidad,habilidad_contrareloj):
        super().__init__(nombre, edad, nacionalidad)
        self.habilidad_contrareloj = habilidad_contrareloj

class EquipoCiclista:
    def __init__(self,nombre):
        self.nombre = nombre
        self.ciclistas = []
        
    def agregar_ciclista(self,ciclista):
        self.ciclistas.append(ciclista)
        