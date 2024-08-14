# Lista inicial de nombres
nombres = [
    "Marie Curie",
    "Cristiano Ronaldo",
    "Nikola Tesla",
    "Roger Federer",
    "Galileo Galilei",
    "Serena Williams",
    "Ada Lovelace",
    "Rafael Nadal",
    "Michael Jordan"
]

# Listas para clasificar los nombres
cientificos = ["Marie Curie", "Nikola Tesla", "Galileo Galilei", "Ada Lovelace"]
deportistas = ["Cristiano Ronaldo", "Roger Federer", "Serena Williams", "Rafael Nadal", "Michael Jordan"]
otros = []

# Función para honrar a los científicos
def honrar_cientificos(lista_cientificos):
    for i in range(len(lista_cientificos)):
        lista_cientificos[i] = "El honorable " + lista_cientificos[i]

# Función para mostrar los nombres
def mostrar_nombres(lista):
    for nombre in lista:
        print(nombre)

# Clasificar los nombres que no están en las listas de científicos o deportistas
for nombre in nombres:
    if nombre not in cientificos and nombre not in deportistas:
        otros.append(nombre)

# Imprimir la lista completa de nombres antes de ser modificados
print("Lista completa de nombres antes de ser modificados:")
mostrar_nombres(nombres)

# Honrar a los científicos
honrar_cientificos(cientificos)

# Imprimir los nombres de los científicos honorables, los deportistas y los restantes
print("\nCientíficos honorables:")
mostrar_nombres(cientificos)

print("\nDeportistas:")
mostrar_nombres(deportistas)

print("\nOtros:")
mostrar_nombres(otros)


