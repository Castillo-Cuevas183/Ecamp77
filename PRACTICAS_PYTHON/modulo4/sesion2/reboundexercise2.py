class Animal:
    def __init__(self, nombre, raza, edad, peso):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso

    def __str__(self):
        return f"Nombre: {self.nombre}, Raza: {self.raza}, Edad: {self.edad}, Peso: {self.peso} kg"

# Creación de la instancia del caballo
caballo = Animal(nombre="Zeus", raza="Pura Sangre", edad="5 años", peso=450)

# Creación de la instancia del león
leon = Animal(nombre="Boulder", raza="Atlas", edad="10 años", peso=130)

# Imprimir la información de cada animal
print("Caballo:")
print(caballo)
print("\nLeón:")
print(leon)
