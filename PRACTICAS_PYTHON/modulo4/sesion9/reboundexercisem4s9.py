def agregar_contenido():
    nombre_archivo = "informacion.dat"
    
    # Abrir el archivo en modo de agregar ('a')
    with open(nombre_archivo, 'a') as archivo:
        archivo.write("Hola Mundo\n")
        archivo.write("Este es una nueva línea en el archivo\n")
        archivo.write("agregando la segunda línea del archivo\n")
        archivo.write("finalizando la línea agregada\n")
    
    print(f"Contenido adicional agregado a '{nombre_archivo}'.")

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

# Agregar contenido y luego imprimir el archivo completo
agregar_contenido()
leer_archivo()
