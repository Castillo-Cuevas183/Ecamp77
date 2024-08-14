# Obtener Datos de Consola
nombre = input("Introduce el nombre del contacto: ")
correo = input("Introduce el correo electrónico del contacto: ")
telefono = input("Introduce el número de teléfono del contacto: ")

# Almacenar Datos en un diccionario
contacto = { "nombre": nombre, 
            "correo": correo, 
            "telefono": telefono
            }

# Operaciones Básicas
total_caracteres_nombre = len(contacto["nombre"])

# Imprimir los resultados
print("\nInformación del contacto:")
print(f"Nombre: {contacto['nombre']}")
print(f"Correo Electrónico: {contacto['correo']}")
print(f"Número de Teléfono: {contacto['telefono']}")
print(f"Número total de caracteres en el nombre: {total_caracteres_nombre}")
