def reemplazar_contenido():
    nombre_archivo = "informacion.dat"
    
    try:
        # Leer el contenido del archivo
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
        
        # Realizar los reemplazos
        nuevo_contenido = contenido.replace("información", "Procesamiento")
        numero_reemplazos = contenido.count("información")
        
        # Escribir el nuevo contenido en el archivo
        with open(nombre_archivo, 'w') as archivo:
            archivo.write(nuevo_contenido)
        
        # Imprimir el número de reemplazos
        print(f"Se realizaron: {numero_reemplazos} reemplazos")
        print(f"El contenido del archivo {nombre_archivo} es:\n")
        print(nuevo_contenido)
    
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no existe.")

# Llamar a la función para reemplazar el contenido y mostrar el resultado
reemplazar_contenido()
