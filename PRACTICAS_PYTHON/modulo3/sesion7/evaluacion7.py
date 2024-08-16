#Lista de diccionarios estudiantes
estudiantes = [
{'nombre': 'Juan', 'edad': 17, 'calificaciones': [85, 90, 88]}, 
{'nombre': 'María', 'edad': 19, 'calificaciones': [92, 89, 90]}, 
{'nombre': 'Pedro', 'edad': 21, 'calificaciones': [85, 95, 80]}, 
{'nombre': 'Ana', 'edad': 18, 'calificaciones': [90, 92, 87]}, 
{'nombre': 'Luis', 'edad': 20, 'calificaciones': [88, 85, 92]},
]

# Función para calcular si un número es primo
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Filtrar y mostrar estudiantes mayores de 18 años con promedio superior a 85
print("Estudiantes mayores de 18 años con promedio superior a 85:")
for estudiante in estudiantes:
    if estudiante['edad'] > 18:
        promedio = sum(estudiante['calificaciones']) / len(estudiante['calificaciones'])
        if promedio > 85:
            print(f"Nombre: {estudiante['nombre']}, Edad: {estudiante['edad']}, Promedio: {promedio:.1f}")


# Calcular promedio de calificaciones de estudiantes mayores de 18 años 
promedios_primos = []
for estudiante in estudiantes:
    if estudiante['edad'] > 18 and es_primo(estudiante['edad']):
        promedio = sum(estudiante['calificaciones']) / len(estudiante['calificaciones'])
        promedios_primos.append(promedio)

# Imprimir promedio total de calificaciones de estudiantes con edad prima
if promedios_primos:
    promedio_final = sum(promedios_primos) / len(promedios_primos)
    print(f"Promedio de calificaciones de estudiantes con edad prima: {promedio_final:.1f}")
else:
    print("No hay estudiantes con edad prima y mayores de 18 años.")