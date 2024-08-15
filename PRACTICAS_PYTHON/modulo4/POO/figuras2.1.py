#Herencia: Todas las figuras heredarán de la clase base "Figura".
class Figura:
    def __init__(self,lados, longitud):
        self.lados = lados
        self.longitud = longitud
        
#Polimorfismo: El método (calcular_perimetro) es compartido por todas las clases derivadas, pero cada una calcula el perímetro en función del número de lados específico.
    def calcular_perimetro(self):
        return self.lados * self.longitud
    
#Definición de las clases derivadas, pero cada una calcula el perímetro
#Uso de super(), Permite reutilizar la lógica de la clase base en las clases derivadas.
class Cuadrado(Figura):
    def __init__(self, longitud):
        super().__init__(4, longitud) 
        
class Pentagono(Figura):
    def __init__(self, longitud):
        super().__init__(5, longitud)

class Octagono(Figura):
    def __init__(self, longitud):
        super().__init__(8, longitud)       
    
    
# Crear instancias y calcular perímetros
octagono = Octagono(10)
pentagono = Pentagono(100)
cuadrado = Cuadrado(1000)

print(octagono.calcular_perimetro()) 
print(pentagono.calcular_perimetro())  
print(cuadrado.calcular_perimetro())  

