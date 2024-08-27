import json

with open("/Users/cristiancastillo/Documents/GitHub/Ecamp77/PRACTICAS_PYTHON/modulo4/files/json/employees.json", "r") as file:
    data = json.load(file)

#Operación Básica
#Mostrar la informacion de un json 
print("------Lista de empleados------")
for employee in data["employees"]:
    print(f"Nombre: {employee['name']}, Edad: {employee['age']} años")
    
#Obtener edad promedio de los empleados
total_age = sum(employee["age"] for employee in data["employees"])
average_age = total_age / len(data["employees"])
print(f"Edad promedio de los empleados: {average_age:.2f} años")

#Encontrar empleados de una ciudad específica
city = "London"
employees_in_city = [emp["name"] for emp in data["employees"] if emp["city"]==city ] 
print(f"\n Empleado en la ciudad {city}: {",".join(employees_in_city)}") #join limpia el archivo para que el resultado no lo entregue como lista
    
#Otra forma de buscar empleados de una ciudad en específica a través de un imput
city = input("Ingrese la ciudad de interés: ")
filtered_employees = [employee for employee in data["employees"] if employee["city"] == city]
print(f"\n------Empleados de la ciudad {city}------")

#Agregar nuevo Empleado
new_employee = {
    "name": "Roberto",
    "age": 38,
    "city": "Tlaxcala" 
}
data["employees"].append(new_employee)

#Guardar los cambios
with open("/Users/cristiancastillo/Documents/GitHub/Ecamp77/PRACTICAS_PYTHON/modulo4/files/json/employees.json", "w") as file:
    json.dump(data, file, indent=4) # almacenar datos JSON directamente en un archivo. Esta función toma dos parámetros: los datos a serializar y el objeto de archivo donde se escribirán los datos.
print("------Empleado agregado correctamente------")



#Filtrar y mostrar los empleados con edad mayor a 30 años
print("\n------Empleados con edad mayor a 30 años------")
for employee in data["employees"]:
    if employee["age"] > 30:
        print(f"Nombre: {employee['name']}, Edad: {employee['age']} años")

#Ordenar la lista de empleados por edad de mayor a menor
sorted_employees = sorted(data["employees"], key=lambda employee: employee["age"], reverse=True)

print("\n------Listado de empleados ordenados por edad de mayor a menor------")
for employee in sorted_employees:
    print(f"Nombre: {employee['name']}, Edad: {employee['age']} años")
    
    