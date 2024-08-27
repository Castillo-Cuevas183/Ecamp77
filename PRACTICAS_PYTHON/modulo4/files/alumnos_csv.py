import csv

#Escribe un csv incluyendo cabecera y los datos
def escribir_csv(filename, datos):
    with open(filename, mode='w', newline='') as file:
        escritor_csv = csv.writer(file) #invocar funcion escribir de la libreria csv
        escritor_csv.writerow(["Nombre", "Apellido", "Ciudad"]) #Cabecera
        for fila in datos: #Iteramos sobre los datos y escribimos cada fila al csv
            escritor_csv.writerow(fila) #Datos
        print("Archivo csv creado con éxito...")

#Lee un csv y muestra los datos
def leer_csv(filename):
    print("Datos del archivo csv:")
    with open(filename, mode='r', newline='') as file:
        lector_csv = csv.reader(file)
        for fila in lector_csv:
            print(fila)

#Agrega Registro al final del archivo 
def agregar_csv(filename,registro):
    with open(filename, mode='a', newline='') as file:
        escritor_csv = csv.writer(file)
        escritor_csv.writerow(registro)
        print("Registro agregado con éxito...")
        

#Ejemplos de datos iniciales
datos_iniciales = [["Moises", "Barrera", "Santiago"], ["Edgar", "Valenzuela", "Osorno"], ["Cristopher", "Sanchez", "Santiago"]]
nombre_archivo = "/Users/cristiancastillo/Documents/GitHub/Ecamp77/PRACTICAS_PYTHON/modulo4/files/csv/students.csv"
registro_agregar = ["Armin", "Cano", "Villarrica" ]
registro_agregar2=["Jose", "Viñuela", "Santiago"]
escribir_csv(nombre_archivo, datos_iniciales)
leer_csv(nombre_archivo)
agregar_csv(nombre_archivo, registro_agregar)
agregar_csv(nombre_archivo, registro_agregar2)

