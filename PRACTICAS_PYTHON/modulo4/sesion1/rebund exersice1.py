# Definición de la clase Animal
class Animal:
    def __init__(self, nombre, raza, edad, peso):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso

    def comer(self):
        print(f"{self.nombre} está comiendo.")

    def caminar(self):
        print(f"{self.nombre} está caminando.")

    def dormir(self):
        print(f"{self.nombre} está durmiendo.")

# Creación del objeto perro
perro = Animal(nombre="Brando", raza="San Bernardo", edad=3, peso=30)

# Creación del objeto gato
gato = Animal(nombre="Roll", raza="Persa", edad=4, peso=3)

# Uso de los métodos para el objeto perro
print(f"Perro: {perro.nombre}, Raza: {perro.raza}, Edad: {perro.edad} años, Peso: {perro.peso} kg.")
perro.comer()
perro.caminar()
perro.dormir()

print("\n")

# Uso de los métodos para el objeto gato
print(f"Gato: {gato.nombre}, Raza: {gato.raza}, Edad: {gato.edad} años, Peso: {gato.peso} kg.")
gato.comer()
gato.caminar()
gato.dormir()
