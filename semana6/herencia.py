# Definimos la clase base Animal
class Animal:
    # Método constructor: se ejecuta al crear una nueva instancia
    def __init__(self, nombre, edad, color):
        self.nombre = nombre      
        self.edad = edad          
        self.color = color        

    # Método de la clase Animal
    def dormir(self):
        return "Durmiendo..."    

# Definimos la clase Perro que hereda de Animal
class Perro(Animal):
    # Constructor de la clase Perro
    def __init__(self, nombre, edad, color, dueño):
        # Llamamos al constructor de la clase base (Animal)
        super().__init__(nombre, edad, color)
        self.dueño = dueño        

    # Método propio de la clase Perro
    def comiendo(self):
        return "Comiendo..."      

# Definimos la clase Tortuga que también hereda de Animal
class Tortuga(Animal):
    # Constructor de la clase Tortuga
    def __init__(self, nombre, edad, color):
        # Llamamos al constructor de la clase base
        super().__init__(nombre, edad, color)

    # Método propio de la clase Tortuga
    def comiendo(self):
        return "Comiendo..."      

# Creamos un objeto de tipo Perro con sus atributos
object1 = Perro("Firualais", 2, "Blanco", True)

# Creamos un objeto de tipo Tortuga con sus atributos
object2 = Tortuga("Erik", 200, "Verde")

# Llamamos al método comiendo en ambos objetos y mostramos el resultado
print(object1.comiendo())  
print(object2.comiendo())  
