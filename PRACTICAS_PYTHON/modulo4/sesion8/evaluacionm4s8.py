nombre_archivo = "informacion.dat"

try:
    # Intentar abrir el archivo en modo lectura
    with open(nombre_archivo, 'r') as archivo:
        print(f"El archivo '{nombre_archivo}' ya existe.")
except FileNotFoundError:
    # Si el archivo no existe, se captura la excepción y se crea el archivo
    with open(nombre_archivo, 'w') as archivo:
        archivo.write("Datos de información en la línea 1\n")
        archivo.write("Datos de información en la línea 2\n")
        archivo.write("Datos de información en la línea 3\n")
        archivo.write("Datos de información en la línea 4\n")
        archivo.write("Datos de información en la línea 5\n")
    print(f"El archivo '{nombre_archivo}' ha sido creado con éxito.")



def leer_archivo():
    nombre_archivo = "informacion.dat"
    
    try:
        # Abrir el archivo en modo lectura
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            print("Contenido del archivo:")
            print(contenido)
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no existe.")

# Llamar a la función para leer el archivo
leer_archivo()
