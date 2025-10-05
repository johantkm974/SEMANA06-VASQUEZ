from abc import ABC, abstractmethod

# Clase abstracta que define un modelo general de transporte
class Transporte(ABC):

    # Método constructor: define atributos comunes
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    # Método abstracto: las subclases deben implementarlo
    @abstractmethod
    def mover(self):
        pass


# Clase concreta Auto que hereda de Transporte
class Auto(Transporte):

    def mover(self):
        return f"El auto {self.marca} modelo {self.modelo} se está moviendo por carretera."


# Clase concreta Barco que hereda de Transporte
class Barco(Transporte):

    def mover(self):
        return f"El barco {self.marca} modelo {self.modelo} navega por el mar."


# Creamos objetos de cada clase
auto1 = Auto("Toyota", "Corolla")
barco1 = Barco("Yamaha", "WaveRunner")

# Mostramos el comportamiento de cada uno
print(auto1.mover())
print(barco1.mover())


