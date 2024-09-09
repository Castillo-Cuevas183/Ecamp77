#PARTE 1

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

# Función principal para crear instancias y mostrar resultados
def main():
    cantidad = int(input("¿Cuántos vehículos desea insertar? "))
    vehiculos = []

    for i in range(cantidad):
        print(f"\nDatos del automóvil {i + 1}")
        marca = input("Inserte la marca del automóvil: ")
        modelo = input("Inserte el modelo: ")
        nro_ruedas = int(input("Inserte el número de ruedas: "))
        velocidad = int(input("Inserte la velocidad en km/h: "))
        cilindrada = int(input("Inserte la cilindrada en cc: "))
        vehiculo = Automovil(marca, modelo, nro_ruedas, velocidad, cilindrada)
        vehiculos.append(vehiculo)

    print("\nImprimiendo por pantalla los Vehículos:")
    for i, vehiculo in enumerate(vehiculos):
        print(f"Datos del automóvil {i + 1}: {vehiculo}")

if __name__ == "__main__":
    main()


