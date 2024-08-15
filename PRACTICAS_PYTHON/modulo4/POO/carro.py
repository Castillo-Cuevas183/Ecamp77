#Definimos la clase Coche
class Coche:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

#Metodos que hace uso de los inicializadores de la clase Coche
#Método describir
    def describir(self):
        return f"Marca: {self.marca}, \nModelo: {self.modelo}, \nAño: {self.anio}"

#Método arrancar
    def arrancar(self):
        return f"el {self.marca}, {self.modelo}, está arrancando"


#Definimos la clase Moto 
class Moto:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio 
#Metodos que hace uso de los inicializadores de la clase Moto
#Método mostrar detalle 
    def mostrar_detalle(self):
        return f"Marca: {self.marca} , \nModelo: {self.modelo}, \nAño: {self.anio}"  
#Método encender
    def encender(self):
        return f"La moto es: {self.marca},{self.modelo} esta arrancando"   
    


#Main
#se crea el objeto mi_coche
mi_coche = Coche("Toyota", "Yaris","2017")

#Mandamos a traer un método de una clase Coche
print(mi_coche.describir())
print(mi_coche.arrancar())

#se crea el objeto mi_moto
mi_moto = Moto("Honda", "CBR","2018")
mi_moto2 = Moto("Yamaha", "250","2022")

#Mandamos a traer un método de una clase Moto
print(mi_moto.mostrar_detalle())
print(mi_moto.encender())


