#copiar el contenido de un archivo a otro

#Método
#r lectura

def copiar_archivo(archivo_origen, archivo_destino):
    try:
        with open(archivo_origen, 'r') as origen:
            contenido=origen.read() #leemos el contenido del origen
            #Abrir archivo destino en modo de lectura
        with open(archivo_destino, 'w') as destino:
            destino.write(contenido) #escribimos el contenido al destino
    except FileNotFoundError:
        print(f"No se encontró el archivo Origen {archivo_origen}")
#contar parlabra de un archivo

def contar_palabra(archivo):
    try:
        with open(archivo, 'r') as f:
            contenido=f.read() #leemos el contenido 
            palabras=contenido.split() #separamos el contenido en palabras
            print(f"el {archivo} contiene {len(palabras)} palabras")
            
    except FileNotFoundError:
        print(f"No se encontró el archivo {archivo}")

def reemplazar_palabra(archivo_origen, palabra_buscar, palabra_reemplazo):
    try:
        with open(archivo_origen, 'r') as origen: #r, se abre archivo en modo lectura 
            contenido=origen.read() #leemos el contenido 
            nuevo_contenido=contenido.replace(palabra_buscar, palabra_reemplazo) #reemplazamos la palabra
            
            #Abrir archivo destino en modo de lectura
        with open(archivo_origen, 'w') as destino:
            destino.write(nuevo_contenido) #escribimos el contenido al destino
            print("palabra modificada")
    except FileNotFoundError:
        print(f"No se encontró el archivo Origen {archivo_origen}")

        
#Main
copiar_archivo ("files/ejemplo3.txt", "files/ejemplo2.txt")
contar_palabra ("files/ejemplo.txt")
reemplazar_palabra("files/ejemplo.txt", "hola", "adios")