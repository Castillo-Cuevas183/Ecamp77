# #Métodos para Cadenas (str)
str.upper()# 
    # Convierte todos los caracteres de la cadena en mayúsculas.



texto = "hola"
print(texto.upper())  # Output# HOLA
str.lower() 
    # Convierte todos los caracteres de la cadena en minúsculas.



texto = "HOLA"
print(texto.lower())  # Output# hola
str.title()# Convierte el primer carácter de cada palabra en mayúscula.



texto = "hola mundo"
print(texto.title())  # Output# Hola Mundo
str.split(texto) 
    # Divide la cadena en una lista de subcadenas, usando el separador sep.



texto = "uno,dos,tres"
print(texto.split(','))  # Output# ['uno', 'dos', 'tres']
str.join(texto)
##Une los elementos de un iterable en una cadena, separados por la cadena original.



lista = ['uno', 'dos', 'tres']
print(', '.join(lista))  # Output# uno, dos, tres
str.replace('uno', 'dos')# Reemplaza todas las apariciones de la subcadena old por new.



texto = "hola mundo"
print(texto.replace("mundo", ""))  # Output# hola 
str.strip()# Elimina los espacios en blanco al principio y al final de la cadena.



texto = "   hola   "
print(texto.strip())  # Output# hola
#Métodos para Listas (list)
list.append(x)# Agrega un elemento x al final de la lista.



lista = [1, 2, 3]
lista.append(4)
print(lista)  # Output# [1, 2, 3, 4]
list.extend(iterable)# Extiende la lista agregando elementos del iterable.



lista = [1, 2, 3]
lista.extend([4, 5])
print(lista)  # Output# [1, 2, 3, 4, 5]
list.insert(index, x)# Inserta un elemento x en la posición index.



lista = [1, 2, 3]
lista.insert(1, 'a')
print(lista)  # Output# [1, 'a', 2, 3]
list.remove(x)# Elimina la primera aparición del elemento x.



lista = [1, 2, 3, 2]
lista.remove(2)
print(lista)  # Output# [1, 3, 2]
list.pop([i])# Elimina y devuelve el elemento en la posición i. Si no se especifica i, elimina y devuelve el último elemento.



lista = [1, 2, 3]
print(lista.pop())  # Output# 3
print(lista)  # Output# [1, 2]
list.sort(key=None, reverse=False)# Ordena los elementos de la lista in-place (por defecto, en orden ascendente).



lista = [3, 1, 2]
lista.sort()
print(lista)  # Output# [1, 2, 3]
list.reverse()# Invierte el orden de los elementos en la lista.



lista = [1, 2, 3]
lista.reverse()
print(lista)  # Output# [3, 2, 1]

##Métodos para Conjuntos (set)
set.add(elem)# Agrega un elemento al conjunto.



conjunto = {1, 2, 3}
conjunto.add(4)
print(conjunto)  # Output# {1, 2, 3, 4}
set.remove(2)# Elimina un elemento del conjunto. Lanza una excepción si el elemento no está presente.



conjunto = {1, 2, 3}
conjunto.remove(2)
print(conjunto)  # Output# {1, 3}
set.discard(3)# Elimina un elemento del conjunto si está presente. No lanza excepción si el elemento no está presente.



conjunto = {1, 2, 3}
conjunto.discard(4)  # No lanza excepción
print(conjunto)  # Output# {1, 2, 3}
set.pop()# Elimina y devuelve un elemento arbitrario del conjunto.



conjunto = {1, 2, 3}
print(conjunto.pop())  # Output# 1 (o 2 o 3, depende del orden interno)
set.union(other)# Devuelve la unión de dos conjuntos.



conjunto1 = {1, 2}
conjunto2 = {2, 3}
print(conjunto1.union(conjunto2))  # Output# {1, 2, 3}
set.intersection(other)# Devuelve la intersección de dos conjuntos.



conjunto1 = {1, 2}
conjunto2 = {2, 3}
print(conjunto1.intersection(conjunto2))  # Output# {2}
set.difference(other)# Devuelve la diferencia entre dos conjuntos.



conjunto1 = {1, 2, 3}
conjunto2 = {2, 3}
print(conjunto1.difference(conjunto2))  # Output# {1}
set.symmetric_difference(other)# Devuelve la diferencia simétrica entre dos conjuntos.



conjunto1 = {1, 2, 3}
conjunto2 = {2, 3, 4}
print(conjunto1.symmetric_difference(conjunto2))  # Output# {1, 4}

# #Métodos para Diccionarios (dict)
dict.get(key, default=None)# Devuelve el valor para la clave key si existe, de lo contrario devuelve default.



diccionario = {"a": 1, "b": 2}
print(diccionario.get("a"))  # Output# 1
print(diccionario.get("c", "no encontrado"))  # Output# no encontrado
dict.keys()# Devuelve una vista de las claves del diccionario.



diccionario = {"a": 1, "b": 2}
print(diccionario.keys())  # Output# dict_keys(['a', 'b'])
dict.values()# Devuelve una vista de los valores del diccionario.



diccionario = {"a": 1, "b": 2}
print(diccionario.values())  # Output# dict_values([1, 2])
dict.items()# Devuelve una vista de los pares clave-valor del diccionario.



diccionario = {"a": 1, "b": 2}
print(diccionario.items())  # Output# dict_items([('a', 1), ('b', 2)])
dict.pop(key, default=None)# Elimina y devuelve el valor para la clave key. Si la clave no existe, devuelve default.



diccionario = {"a": 1, "b": 2}
print(diccionario.pop("a"))  # Output# 1
print(diccionario.pop("c", "no encontrado"))  # Output# no encontrado
dict.update(other)# Actualiza el diccionario con los pares clave-valor del diccionario other.



diccionario = {"a": 1, "b": 2}
diccionario.update({"b": 2})
print(diccionario)  # Output# {'a'# 1, 'b'# 2}
dict.clear()# Elimina todos los elementos del diccionario.



diccionario = {"a": 1, "b": 2}
diccionario.clear()
print(diccionario)  # Output# {}