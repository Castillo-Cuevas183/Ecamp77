
# Definir la palabra original
palabra = "paralelepípedo"

# Crear una lista de vocales
vocales = "aeiouáéíóú"

# Filtrar las consonantes eliminando las vocales
consonantes = [letra for letra in palabra if letra not in vocales]

# Imprimir las consonantes y su posición
for i, letra in enumerate(consonantes):
    print(f"Consonante: {letra}, Posición: {i}")

# Contar la cantidad de consonantes
print(f"\nCantidad de consonantes: {len(consonantes)}")

