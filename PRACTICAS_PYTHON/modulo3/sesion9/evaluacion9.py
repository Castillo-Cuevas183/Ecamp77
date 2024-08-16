# Funciones para operaciones básicas
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Indefinido"  # Manejo de división por cero

# Función que retorna una tupla con todos los resultados
def operaciones(a, b):
    return (suma(a, b), resta(a, b), multiplicacion(a, b), division(a, b))

# Ejemplo de uso
a = 10
b = 40

resultados = operaciones(a, b)

# Almacenar los resultados en un diccionario
resultados_dict = {
    "Suma": resultados[0],
    "Resta": resultados[1],
    "Multiplicación": resultados[2],
    "División": resultados[3]
}

# Imprimir el diccionario con los resultados
print(resultados_dict)
