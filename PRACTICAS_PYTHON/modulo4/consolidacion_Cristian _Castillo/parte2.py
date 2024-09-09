#PARTE 2

# Definición de la clase Vehículo
class Vehiculo:
    def __init__(self, marca, modelo, nro_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.nro_ruedas = nro_ruedas

# Definición de la clase Automóvil que hereda de Vehículo
class Automovil(Vehiculo):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada):
        super().__init__(marca, modelo, nro_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, {self.nro_ruedas} ruedas, {self.velocidad} Km/h, {self.cilindrada} cc"

# Clase Particular que hereda de Automovil
class Particular(Automovil):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada, nro_puestos):
        super().__init__(marca, modelo, nro_ruedas, velocidad, cilindrada)
        self.nro_puestos = nro_puestos

    def __str__(self):
        return super().__str__() + f", Puestos: {self.nro_puestos}"

# Clase Carga que hereda de Automovil
class Carga(Automovil):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada, carga):
        super().__init__(marca, modelo, nro_ruedas, velocidad, cilindrada)
        self.carga = carga

    def __str__(self):
        return super().__str__() + f", Carga: {self.carga} Kg"

# Clase Bicicleta que hereda de Vehiculo
class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, nro_ruedas, tipo):
        super().__init__(marca, modelo, nro_ruedas)
        self.tipo = tipo

    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, {self.nro_ruedas} ruedas, Tipo: {self.tipo}"

# Clase Motocicleta que hereda de Bicicleta
class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, nro_ruedas, tipo, motor, cuadro, nro_radios):
        super().__init__(marca, modelo, nro_ruedas, tipo)
        self.motor = motor
        self.cuadro = cuadro
        self.nro_radios = nro_radios

    def __str__(self):
        return super().__str__() + f", Motor: {self.motor}, Cuadro: {self.cuadro}, Nro Radios: {self.nro_radios}"

def main():
    particular = Particular("Ford", "Fiesta", 4, 180, 500, 5)
    carga = Carga("Daft Trucks", "G 38", 10, 120, 1000, 20000)
    bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
    motocicleta = Motocicleta("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)

    vehiculos = [particular, carga, bicicleta, motocicleta]

    for vehiculo in vehiculos:
        print(vehiculo)

    # Verificación de relaciones de instancia
    print("\nVerificando relaciones de instancia:")
    print("Motocicleta es instancia con relación a Vehículo:", isinstance(motocicleta, Vehiculo))
    print("Motocicleta es instancia con relación a Automovil:", isinstance(motocicleta, Automovil))
    print("Motocicleta es instancia con relación a Particular:", isinstance(motocicleta, Particular))
    print("Motocicleta es instancia con relación a Carga:", isinstance(motocicleta, Carga))
    print("Motocicleta es instancia con relación a Bicicleta:", isinstance(motocicleta, Bicicleta))
    print("Motocicleta es instancia con relación a Motocicleta:", isinstance(motocicleta, Motocicleta))

if __name__ == "__main__":
    main()
