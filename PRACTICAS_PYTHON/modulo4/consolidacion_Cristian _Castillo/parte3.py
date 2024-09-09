import csv

# Clase Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo, nro_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.nro_ruedas = nro_ruedas

    def guardar_datos_csv(self, nombre_archivo):
        try:
            with open(nombre_archivo, mode='a', newline='') as archivo:
                archivo_csv = csv.writer(archivo)
                archivo_csv.writerow([self.__class__.__name__, self.__dict__])
        except IOError as e:
            print(f"Error al guardar en el archivo {nombre_archivo}: {e}")

    @staticmethod
    def leer_datos_csv(nombre_archivo):
        vehiculos = []
        try:
            with open(nombre_archivo, mode='r') as archivo:
                archivo_csv = csv.reader(archivo)
                for row in archivo_csv:
                    vehiculos.append(row)
        except FileNotFoundError:
            print(f"Error: el archivo {nombre_archivo} no existe.")
        except IOError as e:
            print(f"Error al leer el archivo {nombre_archivo}: {e}")
        return vehiculos

# Clase Automovil que hereda de Vehiculo
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

# Función principal para la creación y manejo de vehículos
def main():
    # Crear instancias de diferentes tipos de vehículos
    particular = Particular("Ford", "Fiesta", 4, 180, 500, 5)
    carga = Carga("Daft Trucks", "G 38", 10, 120, 1000, 20000)
    bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
    motocicleta = Motocicleta("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)

    # Lista de vehículos
    vehiculos = [particular, carga, bicicleta, motocicleta]

    # Guardar los datos en un archivo CSV
    for vehiculo in vehiculos:
        vehiculo.guardar_datos_csv('vehiculos.csv')

    # Leer los datos del archivo CSV y mostrarlos
    print("\nLista de Vehículos Guardados en vehiculos.csv:")
    datos_leidos = Vehiculo.leer_datos_csv('vehiculos.csv')
    for dato in datos_leidos:
        print(dato)

if __name__ == "__main__":
    main()
