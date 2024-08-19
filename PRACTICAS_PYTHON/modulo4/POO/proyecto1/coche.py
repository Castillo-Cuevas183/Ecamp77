from vehiculo import Vehiculo

class Coche(Vehiculo):
    def __init__(self, marca, modelo, num_puertas):
        super().__init__(marca, modelo)
        self.num_puertas = num_puertas
    def abrir_puertas(self):
        print(f"El coche {self.marca}, con modelo {self.modelo} abre {self.num_puertas} puertas.")