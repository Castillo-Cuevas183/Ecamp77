#hacer clase vehiculo que tenga los metodos moverse y describirse
#clase hija, moto, auto, bicicleta
# todas las clase hija deber un metodo propio
#usado abstracion y herencia


# Para usar abstracción y herencia, importamos la clase ABC (Abstract Base Class) de la biblioteca abc

from abc import ABC, abstractmethod

# Clase Base abstracta Vehiculo
class Vehiculo(ABC):
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

    @abstractmethod
    def moverse(self):
        pass
    def describirse(self):
        pass 


# Clase hija Moto que hereda de Vehiculo
class Moto(Vehiculo):
    def __init__(self, marca, modelo, anio):
        super().__init__(marca, modelo, anio)
    
    def moverse(self):
        return f"La moto {self.marca} {self.modelo} está en movimiento."
    
    def describirse(self):
        return f"Marca: {self.marca}, \nModelo: {self.modelo}, \nAño: {self.anio}"

    def hacer_piruetas(self):
        return f"La moto {self.marca} {self.modelo} está haciendo piruetas."


# Clase hija Auto que hereda de Vehiculo
class Auto(Vehiculo):
    def __init__(self, marca, modelo, anio):
        super().__init__(marca, modelo, anio)

    def moverse(self):
        return f"El auto {self.marca} {self.modelo} está en movimiento."
    
    def describirse(self):
        return f"Marca: {self.marca}, \nModelo: {self.modelo}, \nAño: {self.anio}"

    def encender_luces(self):
        return f"El auto {self.marca} {self.modelo} está con las luces encendidas."


# Clase hija Bicicleta que hereda de Vehiculo
class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, anio):
        super().__init__(marca, modelo, anio)
        
    def moverse(self):
        return f"La bicicleta {self.marca} {self.modelo} está en movimiento."
    
    def describirse(self):
        return f"Marca: {self.marca}, \nModelo: {self.modelo}, \nAño: {self.anio}"

    def tocar_timbre(self):
        return f"La bicicleta {self.marca} {self.modelo} está tocando el timbre."


# Main
# Se crean instancias de las clases derivadas
mi_moto = Moto("Honda", "CBR", 2018)
mi_auto = Auto("Toyota", "Yaris", 2017)
mi_bicicleta = Bicicleta("Trek", "Marlin 5", 2024)

# Usar los métodos
print(mi_moto.describirse())
print(mi_moto.moverse())
print(mi_moto.hacer_piruetas())

print(mi_auto.describirse())
print(mi_auto.moverse())
print(mi_auto.encender_luces())

print(mi_bicicleta.describirse())
print(mi_bicicleta.moverse())
print(mi_bicicleta.tocar_timbre())
