# Módulo necesario para crear clases abstractas
from abc import ABC, abstractmethod

# Clase abstracta base
class Padre(ABC):
    # Constructor abstracto → define atributos comunes que las subclases deben inicializar
    @abstractmethod
    def __init__(self, nombre, edad, telefono, correo):
        # Atributos de instancia
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono
        self.correo = correo

    # Método abstracto → toda subclase está obligada a implementarlo
    @abstractmethod
    def informacion(self):
        pass


# Clase hija que hereda de Padre
class Hijo(Padre):
    # Constructor concreto → implementa el constructor abstracto del padre
    def __init__(self, nombre, edad, telefono, correo, apodo, profesion):
        # Llamamos al constructor del padre para heredar sus atributos
        super().__init__(nombre, edad, telefono, correo)
        # Atributos propios de la subclase
        self.apodo = apodo
        self.profesion = profesion

    # Implementación del método abstracto del padre
    def informacion(self):
        return f"""
👤 Información del Hijo
Nombre     : {self.nombre}
Edad       : {self.edad} años
Teléfono   : {self.telefono}
Correo     : {self.correo}
Apodo      : {self.apodo}
Profesión  : {self.profesion}
"""



#  Creación de objetos

object1 = Hijo("Johan", 23, 97458547, "johan@gmail.com", "Gohan", "Ingeniero de Software")
object2 = Hijo("Camila", 19, 98562478, "camila@gmail.com", "Cami", "Diseñadora Gráfica")


# Salida del programa

print(object1.informacion())
print(object2.informacion())

