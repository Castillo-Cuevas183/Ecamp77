class A:
    def __init__(self):
        print("Pertenezco a la clase A")
    
    def metodo_a(self):
        print("Método heredado de A")

class B:
    def __init__(self):
        print("Clase B")
    
    def metodo_b(self):
        print("Método heredado de B")

# Definición de la clase C con herencia múltiple
class C(B, A):
    def __init__(self):
        super().__init__()  # Llama al constructor de la clase B
        print("Método es de C")
    
    def metodo_c(self):
        print("Método de clase C")

# Crear una instancia de la clase C
objeto_c = C()

# Acceder a los métodos de la clase C y sus clases base
objeto_c.metodo_a()  # Salida: Método heredado de A
objeto_c.metodo_b()  # Salida: Método heredado de B
objeto_c.metodo_c()  # Salida: Método de clase C
