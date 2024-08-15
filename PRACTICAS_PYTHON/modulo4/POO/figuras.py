class Figuras:
    def calcular_perimetro():
        pass
    class Cuadrado():
        def perimetro(self, lado):
            return lado * 4
    class Pentagono():
        def perimetro(self, lado):
            return lado * 5
    class Exagono():
        def perimetro(self, lado):
            return lado * 6
    class Octagono():
        def perimetro(self, lado):
            return lado * 8
    
    octagono= Octagono ()
    pentagono= Pentagono ()
    exagono= Exagono ()
    cuadrado= Cuadrado ()
    
    print(octagono.perimetro(5))
    print(pentagono.perimetro(7))
    print(exagono.perimetro(9))
        

    
    
    
    
    
    
    """def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    
    def area_cuadrado(self):
        return self.base * self.base

    def area_rectangulo(self):
        return self.base * self.altura
    
    def area_triangulo(self):
        return (self.base * self.altura) / 2
    
    def area_circulo(self, radio):
        import math
        return math.pi * (radio ** 2)
    
    def area_poligono(self, lados, areas):
        return sum(areas) / len(areas)"""
    