#listas (list)
frutas = ["Tunas", "Guanabana", "Maracuyas"]
numerosPrimos = [2, 3, 5, 7, 11]
print(type(frutas))
print(type(numerosPrimos))
print(frutas[0])
print(numerosPrimos[2])

frutas[0]= "Mango"
print(frutas)

#agregar elementos a una lista
frutas.append("Pera")
print(frutas)

#remover elementos de una lista
frutas.remove("Guanabana")
print(frutas)

#slicing de listas
print(frutas[1:3])

#ordenar una lista  
frutas.sort()
print(frutas)