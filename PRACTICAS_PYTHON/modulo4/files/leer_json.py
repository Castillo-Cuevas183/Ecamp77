import json

with open("/Users/cristiancastillo/Documents/GitHub/Ecamp77/PRACTICAS_PYTHON/modulo4/files/json/data.json", "r") as file:
    datos=json.load(file)
nombre = datos["nombre"]
edad = datos["edad"]
correo = datos["correo"]
hobbies = datos["hobbies"]
trabajo = datos["trabajo"]

print(f"Nombre: {nombre}")
print(f"Edad: {edad} años")
print(f"Correo Electrónico: {correo}")
print(f"Hobbies:{hobbies}")
print(f"Trabajo: {trabajo}")


# #1. Mostrar todos los empleados

print("Lista de los empleados:")
for employee in datos ["trabajo"]:
    print(f"Nombre: {trabajo['empresa']}, Empresa: {trabajo['puesto']}, Años: {trabajo['años']}")

    