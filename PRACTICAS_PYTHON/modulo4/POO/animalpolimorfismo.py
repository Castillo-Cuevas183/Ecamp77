#Se declara la clase padre
class Animal:
#    def __init__(self, name):
#        self.name = name
        
    def hacer_sonido(self): 
        pass

#Se declaran las clases hijos
class Perro(Animal):
    def hacer_sonido(self): 
        return "El perro ladra Wuau!"

class Gato(Animal):
    def hacer_sonido(self):
        return "El gato maulla Miau!"

class Vaca(Animal):
    def hacer_sonido(self): 
        return "La vaca hace Moo!"

#metodo que recibe el objeto para que realice el método de la clase "Padre, en este caso Animal"

def animal_sonido(objeto):
    print(objeto.hacer_sonido())

# se crean los objetos         
perro=Perro()
gato= Gato()
vaca=Vaca()
#print(perro.name)
#print(gato.name)
#print(vaca.name)

#Mandamos a traer un método de una clase Padre 
#En este caso, el método de la clase Animal es llamado por cada objeto hijo, 
#mostrando el sonido que produce cada animal.
animal_sonido(perro)
animal_sonido(gato)
animal_sonido(vaca)

#Haciendo una lista solo se hace una variable u objeto en este caso animales lo cual estaría reemplazando lo de las líneas 28 a 30
animales =[Perro(), Gato(), Vaca(), Perro()]
for animal in animales:
    animal_sonido(animal)