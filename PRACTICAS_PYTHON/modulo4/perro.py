#Definimos la Clase

class Dog:
    def __init__(self, name, raza):
        self.name = name
        self.raza = raza

#Metodos que hace uso de los inicializadores
#método ladrar
    def ladrar(self):
            print(f"El perro {self.name}, ladra woof, y es de raza {self.raza}")

#metodo salir a pasear
    def pasear(self):
            print(f"El perro {self.name}, de raza {self.raza}, salio a pasear al parque")

#metodo comer 
    def comer(self):
            print(f"El perro {self.name}, de raza {self.raza}, come croquetas de pollo ")

#Main 

#Creando el objeto 
perro= Dog("Jefazo", "labrador")
perro2= Dog("Philip", "Schnauzer")

#Mandamos a traer un método de una clase  
perro.ladrar()
perro.pasear()
perro.comer()
perro2.ladrar()
perro2.pasear()
perro2.comer()


