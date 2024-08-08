
# Descripción: Devuelve el valor para la clave especificada. Si la clave no existe, devuelve el valor por defecto proporcionado.


diccionario = {'nombre': 'Juan', 'edad': 30}
print(diccionario.get('nombre'))  # Output: Juan
print(diccionario.get('altura', 'No especificado'))  # Output: No especificado
dict.keys()

# Descripción: Devuelve una vista de todas las claves del diccionario.

diccionario = {'nombre': 'Juan', 'edad': 30}
print(diccionario.keys())  # Output: dict_keys(['nombre', 'edad'])
dict.values()

# Descripción: Devuelve una vista de todos los valores del diccionario.

diccionario = {'nombre': 'Juan', 'edad': 30}
print(diccionario.values())  # Output: dict_values(['Juan', 30])


# Descripción: Devuelve una vista de pares clave-valor del diccionario.

diccionario = {'nombre': 'Juan', 'edad': 30}
print(diccionario.items())  # Output: dict_items([('nombre', 'Juan'), ('edad', 30)])


# Descripción: Actualiza el diccionario con los pares clave-valor de other, sobrescribiendo los valores existentes para las claves que ya estaban presentes.

diccionario = {'nombre': 'Juan', 'edad': 30}
diccionario.update({'edad': 31, 'ciudad': 'Madrid'})
print(diccionario)  # Output: {'nombre': 'Juan', 'edad': 31, 'ciudad': 'Madrid'}


# Descripción: Elimina la clave especificada y devuelve su valor. Si la clave no existe, devuelve el valor por defecto proporcionado.

diccionario = {'nombre': 'Juan', 'edad': 30}
edad = diccionario.pop('edad', 'No especificado')
print(edad)  # Output: 30
print(diccionario)  # Output: {'nombre': 'Juan'}


# Descripción: Elimina y devuelve un par clave-valor aleatorio del diccionario. 
# Esta operación es útil para la implementación de algoritmos que necesitan eliminar elementos de un diccionario de manera eficiente.


diccionario = {'nombre': 'Juan', 'edad': 30}
item = diccionario.popitem()
print(item)  # Output: ('edad', 30) o ('nombre', 'Juan')
print(diccionario)  # Output dependerá del item removido


# Descripción: Elimina todos los elementos del diccionario.

diccionario = {'nombre': 'Juan', 'edad': 30}
diccionario.clear()
print(diccionario)  # Output: {}


# Descripción: Devuelve una copia superficial del diccionario.

diccionario = {'nombre': 'Juan', 'edad': 30}
copia_diccionario = diccionario.copy()
print(copia_diccionario)  # Output: {'nombre': 'Juan', 'edad': 30}

# Descripción: Crea un nuevo diccionario con claves de seq y valores establecidos en value.
claves = ['nombre', 'edad', 'ciudad']
diccionario = dict.fromkeys(claves, 'No especificado')
print(diccionario)  # Output: {'nombre': 'No especificado', 'edad': 'No especificado', 'ciudad': 'No especificado'}
