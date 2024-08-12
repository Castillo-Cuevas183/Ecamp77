##Descripción: Agrega un ítem al final de la lista.

lista = [1, 2, 3]
lista.append(4)
print(lista)  # Output: [1, 2, 3, 4]

##Descripción: Extiende la lista agregando todos los ítems de un iterable (como otra lista).

lista = [1, 2, 3]
lista.extend([4, 5])
print(lista)  # Output: [1, 2, 3, 4, 5]


##Descripción: Inserta un ítem en una posición específica. El primer argumento es el índice de la lista donde se inserta el ítem.


lista = [1, 2, 3]
lista.insert(1, 1.5)
print(lista)  # Output: [1, 1.5, 2, 3]


##Descripción: Elimina el primer ítem de la lista cuyo valor sea x. Lanza un ValueError si no existe tal ítem.

lista = [1, 2, 3, 2]
lista.remove(2)
print(lista)  # Output: [1, 3, 2]


##Descripción: Elimina y devuelve el ítem en la posición i. Si no se especifica un índice, pop() elimina y devuelve el último ítem de la lista.

lista = [1, 2, 3]
item = lista.pop(1)
print(item)  # Output: 2
print(lista)  # Output: [1, 3]


##Descripción: Elimina todos los ítems de la lista.

lista = [1, 2, 3]
lista.clear()
print(lista)  # Output: []


##Descripción: Devuelve el índice basado en cero del primer ítem cuyo valor sea x. Lanza un ValueError si no existe tal ítem. Los argumentos opcionales start y end permiten limitar la búsqueda a una subsecuencia específica de la lista.

lista = [1, 2, 3, 2]
index = lista.index(2)
print(index)  # Output: 1
list.count(x)
##Descripción: Devuelve el número de veces que x aparece en la lista.

lista = [1, 2, 2, 3]
count = lista.count(2)
print(count)  # Output: 2

##Descripción: Ordena los ítems de la lista en su lugar (los argumentos se pueden usar para personalizar el orden de la lista).


lista = [3, 1, 2]
lista.sort()
print(lista)  # Output: [1, 2, 3]


##Descripción: Invierte los elementos de la lista en su lugar.

lista = [1, 2, 3]
lista.reverse()
print(lista)  # Output: [3, 2, 1]


##Descripción: Devuelve una copia superficial de la lista.

lista = [1, 2, 3]
copia_lista = lista.copy()
print(copia_lista)  # Output: [1, 2, 3]


#Descripción: Permite obtener una sublista de la lista original.

lista = [1, 2, 3, 4, 5]
sublista = lista[1:4]
print(sublista)  # Output: [2, 3, 4]
