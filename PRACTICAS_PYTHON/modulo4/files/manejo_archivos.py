#sobreescribiendo archivo txt
with open('/Users/cristiancastillo/Documents/GitHub/Ecamp77/PRACTICAS_PYTHON/modulo4/files/ejemplo.txt',"w")as archivo:
    archivo.write("Hola desde Chile \n")
    archivo.write("esta es una línea nueva\n")
    archivo.write("Esto es otra línea")

#leer archivo
with open("/Users/cristiancastillo/Documents/GitHub/Ecamp77/PRACTICAS_PYTHON/modulo4/files/ejemplo.txt","r") as lectura:
    contenido = lectura.read()
    print(contenido)
#Manejo de errores
with open("/Users/cristiancastillo/Documents/GitHub/Ecamp77/PRACTICAS_PYTHON/modulo4/files/ejemplo2.txt","r") as file:
    try:
        contenido = file.read()
        print(contenido)
    except FileNotFoundError:
        print("El archivo no existe")

# with open("/Users/cristiancastillo/Documents/GitHub/Ecamp77/PRACTICAS_PYTHON/modulo4/files/ejemplo.txt", "r") as archivo:
#     contador=0
#     for linea in archivo:
#     contador += 1  #contador = contador + 1  #suma = numero  + suma
# print(f"el archivo tiene {linea.strip()} lineas")