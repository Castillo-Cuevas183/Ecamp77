# Obtener Datos de Consola
nombre1 = input("Nombre de la primera persona: ")
edad1 = int(input(f"Ingrese la edad de {nombre1}: "))
altura1 = float(input(f"Ingrese la altura de {nombre1} en metros: "))

nombre2 = input("Nombre de la segunda persona: ")
edad2 = int(input(f"Ingrese la edad de {nombre2}: "))
altura2 = float(input(f"Ingrese la altura de {nombre2} en metros: "))

nombre3 = input("Nombre de la tercera persona: ")
edad3 = int(input(f"Ingrese la edad de {nombre3}: "))
altura3 = float(input(f"Ingrese la altura de {nombre3} en metros: "))

# Calcular Promedios y Totales

# Promedio de las edades
promedio_edad = (edad1 + edad2 + edad3) / 3

# Promedio de las alturas
promedio_altura = (altura1 + altura2 + altura3) / 3

# Total de caracteres en los nombres
total_caracteres = len(nombre1) + len(nombre2) + len(nombre3)

# Mostrar Resultados

print(f"\nEl promedio de las edades es: {promedio_edad:.2f} años")
print(f"\nEl promedio de las alturas es: {promedio_altura:.2f} metros")
print(f"\nEl total de caracteres en los nombres es: {total_caracteres}")
