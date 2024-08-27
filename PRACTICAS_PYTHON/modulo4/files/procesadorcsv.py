import csv

class ProcesadorCsv:
    def __init__(self, archivo_entrada, archivo_salida):
        self.archivo_entrada = archivo_entrada
        self.archivo_salida = archivo_salida
        self.datos = []
        
    def leer_datos(self):
        "lee los datos de los archivos"
        with open(self.archivo_entrada, mode='r', newline='') as file:
            reader = csv.DictReader(file) #funcion DictReader invoca un diccionario
            self.datos= [fila for fila in reader]

    def calcular_promedio_general(self):
        total_promedio =sum(float(estudiante["Promedio"]) for  estudiante in self.datos)
        cantidad_estudiante = len(self.datos)
        return total_promedio / cantidad_estudiante if cantidad_estudiante  > 0 else 0
        
    def guardar_resumen(self):
        promedio_general=self.calcular_promedio_general ()
        with open(self.archivo_salida, mode='w', newline='') as file:
            escritor= csv.writer(file)
            escritor.writerow(["Promedio General"])
            escritor.writerow([promedio_general])
            
    
    def procesar(self):
        self.leer_datos()
        self.guardar_resumen()
        print("El procesamiento fue realizado correctamente")
#Main
procesador = ProcesadorCsv("/Users/cristiancastillo/Documents/GitHub/Ecamp77/PRACTICAS_PYTHON/modulo4/files/csv/resumen_estudiantes.csv", "/Users/cristiancastillo/Documents/GitHub/Ecamp77/PRACTICAS_PYTHON/modulo4/files/csv/resumen_estudiantes.csv")
procesador.procesar()

