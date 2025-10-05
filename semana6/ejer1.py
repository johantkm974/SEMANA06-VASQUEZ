class Animal:
    # Método especial constructor: inicializa los atributos del objeto
    def __init__(self, nombre, color, edad, especie, peso, habitat):
        self.nombre = nombre
        self.color = color
        self.edad = edad
        self.especie = especie
        self.peso = peso           # en kilogramos
        self.habitat = habitat     # ejemplo: "selva", "sabana", etc.

    # Método especial: representación legible (para usuarios)
    def __str__(self):
        return f"""Información del Animal
Nombre   : {self.nombre}
Color    : {self.color}
Edad     : {self.edad} años
Especie  : {self.especie}
Peso     : {self.peso} kg
Hábitat  : {self.habitat}
"""

    # Método especial: representación técnica (para desarrolladores)
    def __repr__(self):
        return (
            f"Animal('{self.nombre}', '{self.color}', {self.edad}, "
            f"'{self.especie}', {self.peso}, '{self.habitat}')"
        )

    # Método normal: acción del animal
    def dormir(self):
        return f"{self.nombre} está durmiendo..."

    # Método normal: simular que el animal come
    def comer(self, alimento):
        return f"{self.nombre} está comiendo {alimento}."

    # Método especial: comparación por edad (==)
    def __eq__(self, otro):
        if isinstance(otro, Animal):
            return self.edad == otro.edad
        return False

    # Método especial: comparación por peso (<)
    def __lt__(self, otro):
        if isinstance(otro, Animal):
            return self.peso < otro.peso
        return False


# 🔹 Ejemplo de uso
animal1 = Animal("Lobo", "Gris", 5, "Canino", 35.5, "Bosque")
animal2 = Animal("Tigre", "Naranja", 5, "Felino", 220.7, "Selva")

# Mostrar información
print(animal1)
print(animal1.dormir())
print(animal1.comer("carne"))
print("informacion", repr(animal1))
