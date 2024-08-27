#leer un archivo csv
import csv 
with open("/Users/cristiancastillo/Documents/GitHub/Ecamp77/PRACTICAS_PYTHON/modulo4/files/csv/people.csv", mode="r", newline="") as archivo:
    lector_csv = csv.reader(archivo)
    for fila in lector_csv:
        print(fila)
        
#Escribir en archivo csv
with open("/Users/cristiancastillo/Documents/GitHub/Ecamp77/PRACTICAS_PYTHON/modulo4/files/csv/people2.csv", mode="w", newline="") as file:
    escritor_csv = csv.writer(file)
    escritor_csv.writerow(["Nombre", "Apellido", "Ciudad"])
    escritor_csv.writerow(["Fernando", "Ruiz", "Osorno"])
    escritor_csv.writerow(["Eduardo", "Valenzuela", "Antofagasta"])
    escritor_csv.writerow(["Nicole", "Rodriguez", "Temuco"])

# Agregar un registro a un archivo csv
with open("/Users/cristiancastillo/Documents/GitHub/Ecamp77/PRACTICAS_PYTHON/modulo4/files/csv/people2.csv", mode="a", newline="") as f:
    escritor_csv = csv.writer(f)
    escritor_csv.writerow(["Cristian", "Castillo", "Concepcion"])
    escritor_csv.writerow(["Andrea", "Garcia", "Valparaiso"])
    
    
    