# Lista inicial con todos los nombres
nombres = [
    "Harry Houdini",
    "Newton",
    "David Blaine",
    "Hawking",
    "Messi",
    "Teller",
    "Einstein",
    "Pele",
    "Juanes"
]

# Listas iniciales para cada grupo
magos = ["Harry Houdini", "David Blaine", "Teller"]
cientificos = ["Newton", "Hawking", "Einstein"]
otros = []

#escribir una función llamada hacer_grandioso(), que modifique la lista de magos añadiendo la
#frase ‘El gran‘ antes del nombre de cada mago. 

def hacer_grandioso(lista):
    for i in range(len(lista)):
        lista[i] = "El gran " + lista[i]
    return lista

#Crear una función llamada imprimir_nombres(), que imprime el nombre de cada persona de la
#lista.


# Función para imprimir los nombres según la lista
def imprimir_nombres(lista, titulo):
    print(f"\n{titulo}:")
    for nombre in lista:
        print(nombre)

# Clasificar los nombres que no están en magos ni en científicos
for nombre in nombres:
    if nombre not in magos and nombre not in cientificos:
        otros.append(nombre)

# Imprimir la lista completa de nombres antes de ser modificados
print("Lista completa de nombres antes de ser modificados:")
for nombre in nombres:
    print(nombre)

# Hacer grandiosos a los magos
hacer_grandioso(magos)

# Imprimir los nombres de los magos grandiosos, los científicos y los otros
imprimir_nombres(magos, "Magos grandiosos")
imprimir_nombres(cientificos, "Científicos")
imprimir_nombres(otros, "Restantes")