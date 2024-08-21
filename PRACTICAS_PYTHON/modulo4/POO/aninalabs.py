from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

class Pig(Animal):
    def comer(self):  #error ya que el metodo abstracto deben tener el mismo def  
        return "Oink!"

#MAIN
perro=Dog
gato=Cat
cerdo=Pig


print(perro.sound())
print(gato.sound())
print(cerdo.comer()) # debe reportar error 
