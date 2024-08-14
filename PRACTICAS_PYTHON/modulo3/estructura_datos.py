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

numerosPrimos.append(13)
print(numerosPrimos)    

#tuple (tuple)
dimensiones = (1920, 1080)
coordenadas =(10,20)
print(type(dimensiones))
print(type(coordenadas))
puntos=(10,20)
#puntos[1]=30 #error, los tuples no son mutable

#cojunto 
colores = {"rojo", "verde", "blanco", "rojo"}
numeros_unicos = {1, 2, 3, 4, 5,1}
print(type(colores))
print(colores)
print(type(numeros_unicos))
print(numeros_unicos)
numeros_unicos.add(6)
colores.remove("blanco")
print(colores)
print(len(numeros_unicos))
print(len(colores))

#Dictionaries (dict)
personas = {"nombre": "Juan", "apellido": "Perez", "edad": 25, "ciudad":"Tlaxcala"}
precios = {"manzana":12, "banana":8, "cereza":2.5}
print(type(personas))
print(type(precios))
print(personas["nombre"])
print(precios["manzana"])

personas["edad"] = 31 #modificar un valor
print(personas)
personas["ocupacion"] = "programador" #agregar un nuevo valor
print(personas)



