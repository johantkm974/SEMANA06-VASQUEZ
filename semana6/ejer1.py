#Clase Animal
class Animal:
#Metodo especial constructor se define los atributos de instancia
    def __init__(self,nombre,color, edad):
        self.nombre=nombre
        self.color=color
        self.edad= edad

#Metodo especial debuelbe un cadena
    def __str__(self):
        return f"""
Informacion:
Nombre ={self.nombre}
Color ={self.color}
Edad = {self.edad}
"""
#Metodo epecial de devuelve una dadena con mas datos 
    def __repr__(self):
        return f"""
Nombre ={self.nombre}(str) not null
Color ={self.color}(str) not null
Edad = {self.edad}(int) not null 
"""
#Metodon dormnir de la clase Animal
    def dormir(self):
        return "durmiendo.."
    
object1=Animal("Lobo","gris",2)
    
print(object1)
print(object1.dormir())
print(repr(object1))