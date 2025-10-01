# Importamos los módulos necesarios para usar clases abstractas
from abc import ABC, abstractmethod

# Definimos la clase abstracta Padre, que hereda de ABC (Abstract Base Class)
class Padre(ABC):

    # Método constructor abstracto: obliga a las subclases a implementarlo
    @abstractmethod
    def __init__(self, nombre, edad, telefono, correo):
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono
        self.correo = correo

    # Método abstracto que debe ser implementado por cualquier clase hija
    @abstractmethod
    def informacion(self):
        pass

# Definimos la clase Hijo, que hereda de Padre
class Hijo(Padre):

    # Implementamos el constructor, incluyendo el nuevo atributo 'apodo'
    def __init__(self, nombre, edad, telefono, correo, apodo):
        # Llamamos al constructor de la clase padre para inicializar los atributos heredados
        super().__init__(nombre, edad, telefono, correo)
        # Inicializamos el nuevo atributo propio de la clase Hijo
        self.apodo = apodo

    # Implementamos el método informacion que estaba como abstracto en la clase Padre
    def informacion(self):
        return f"""
Nombre : {self.nombre}
Edad : {self.edad}
Teléfono: {self.telefono}
Correo: {self.correo}
Apodo: {self.apodo}
"""

# Creamos un objeto de la clase Hijo con datos de ejemplo
object1 = Hijo("Johan", 23, 97458547, "johan@gmail.com", "gohan")

# Salida  de mi objeto llamando al metodo informacion()
print(object1.informacion())
