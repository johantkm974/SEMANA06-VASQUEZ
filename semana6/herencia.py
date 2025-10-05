# Clase base o "padre"
class Animal:
    # Constructor: define los atributos de instancia comunes
    def __init__(self, nombre, edad, color, especie, habitat):
        # Atributos de instancia → cada objeto tendrá sus propios valores
        self.nombre = nombre
        self.edad = edad
        self.color = color
        self.especie = especie
        self.habitat = habitat

    # Método compartido por todas las subclases
    def dormir(self):
        return f"{self.nombre} está durmiendo..."

    # Método genérico que puede ser sobrescrito por las subclases
    def hacer_sonido(self):
        return "Hace un sonido..."


# Clase hija: Perro hereda de Animal
class Perro(Animal):
    # Constructor: extiende el del padre con nuevos atributos
    def __init__(self, nombre, edad, color, especie, habitat, raza, dueño):
        # super() llama al constructor de la clase base (Animal)
        super().__init__(nombre, edad, color, especie, habitat)
        # Nuevos atributos exclusivos del Perro
        self.raza = raza
        self.dueño = dueño

    # Métodos propios del Perro
    def comiendo(self):
        return f"{self.nombre} está comiendo croquetas."

    def ladrar(self):
        return f"{self.nombre} dice: ¡Guau guau!"
    
    # Clase hija: Tortuga hereda de Animal
class Tortuga(Animal):
    def __init__(self, nombre, edad, color, especie, habitat, tamaño):
        # Llamamos al constructor de la clase base (Animal)
        super().__init__(nombre, edad, color, especie, habitat)
        # Atributo exclusivo de la clase Tortuga
        self.tamaño = tamaño  # en centímetros

    # Métodos propios de la Tortuga
    def comiendo(self):
        return f"{self.nombre} está comiendo lechuga."

    def moverse_lento(self):
        return f"{self.nombre} se mueve lentamente por el {self.habitat}."
    
    # Objeto de tipo Perro → hereda atributos de Animal y añade los suyos
perro = Perro("Firulais", 4, "Marrón", "Canino", "Casa", "Labrador", "Carlos")

# Objeto de tipo Tortuga → también hereda de Animal
tortuga = Tortuga("Erik", 120, "Verde", "Reptil", "Laguna", 80)


print(" --- Información del Perro ---")
print(f"Nombre: {perro.nombre}")
print(f"Edad: {perro.edad} años")
print(f"Color: {perro.color}")
print(f"Raza: {perro.raza}")
print(f"Dueño: {perro.dueño}")
print(perro.comiendo())
print(perro.ladrar())
print(perro.dormir())

print("\n --- Información de la Tortuga ---")
print(f"Nombre: {tortuga.nombre}")
print(f"Edad: {tortuga.edad} años")
print(f"Tamaño: {tortuga.tamaño} cm")
print(f"Hábitat: {tortuga.habitat}")
print(tortuga.comiendo())
print(tortuga.moverse_lento())
print(tortuga.dormir())

