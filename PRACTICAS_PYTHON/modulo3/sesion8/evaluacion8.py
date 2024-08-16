# Lista de listas
listas = [[1, 2, 3], [0, 4, 5], [4, 0, 1], [6, 5, 4]]

# Diccionario para almacenar las sublistas con claves A, B, C, D
diccionario_sublistas = {}

# Letras para las claves del diccionario
claves = ['A', 'B', 'C', 'D']

# Recorrer la lista de listas
for i, sublista in enumerate(listas):
    if sublista[0] == 0:
        continue  # Omitir la sublista si el primer número es cero
    
    # Crear una nueva sublista omitiendo los ceros que no estén en la primera posición
    nueva_sublista = [num for num in sublista if num != 0]
    
    # Asignar la sublista al diccionario con la clave correspondiente
    diccionario_sublistas[claves[i]] = nueva_sublista

# Imprimir el diccionario resultante de las sublista 
for clave, valor in diccionario_sublistas.items():
    print(f"{clave}: {valor}")
