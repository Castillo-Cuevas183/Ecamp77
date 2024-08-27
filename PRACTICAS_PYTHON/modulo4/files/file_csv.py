import csv 

with open("/Users/cristiancastillo/Documents/GitHub/Ecamp77/PRACTICAS_PYTHON/modulo4/files/csv/alumnos.csv", "r") as archivo_csv:
    lector=csv.reader(archivo_csv)
    for fila in lector:
        print(fila)

#Escribir en un archivo csv
datos=[["Nombre", "Edad"], ["Edgar",24], ["Gonzalo",33]]
with open("nuevos_datos.csv", "w", newline="" ) as archivo_csv
    escribir=csv 
    
        

