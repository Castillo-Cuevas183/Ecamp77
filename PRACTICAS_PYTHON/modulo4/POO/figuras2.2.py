class Figura:
    def __init__(self, lados, longitud_lado):
        self._lados = lados
        self._longitud_lado = longitud_lado
    
    @property
    def lados(self):
        return self._lados
    
    @lados.setter
    def lados(self, value):
        self._lados = value
    
    @property
    def longitud_lado(self):
        return self._longitud_lado
    
    @longitud_lado.setter
    def longitud_lado(self, value):
        self._longitud_lado = value
    
    def calcular_perimetro(self):
        return self.lados * self.longitud_lado

class Cuadrado(Figura):
    def __init__(self, longitud_lado):
        super().__init__(4, longitud_lado)

class Pentagono(Figura):
    def __init__(self, longitud_lado):
        super().__init__(5, longitud_lado)

class Exagono(Figura):
    def __init__(self, longitud_lado):
        super().__init__(6, longitud_lado)

class Octagono(Figura):
    def __init__(self, longitud_lado):
        super().__init__(8, longitud_lado)

# Crear instancias y calcular perímetros
octagono = Octagono(5)
pentagono = Pentagono(5)

# Imprimir perímetros
print(octagono.calcular_perimetro())  # Salida: 40
print(pentagono.calcular_perimetro())  # Salida: 25

# Acceder y modificar propiedades
print(octagono.lados)  # Salida: 8
octagono.longitud_lado = 6
print(octagono.calcular_perimetro())  # Salida: 48
