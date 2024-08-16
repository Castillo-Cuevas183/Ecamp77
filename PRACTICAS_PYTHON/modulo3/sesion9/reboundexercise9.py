def calcular_area_rectangulo():
    try:
        # Solicitar la base y la altura al usuario
        base = float(input("Ingresa la base del rectángulo: "))
        altura = float(input("Ingresa la altura del rectángulo: "))

        # Validar valores positivos
        if base > 0 and altura > 0:
            area = base * altura
            print(f"El área del rectángulo es: {area}")
        else:
            print("Ambos valores deben ser números positivos.")
    except ValueError:
        print("Por favor, ingresa valores numéricos válidos.")

# Llamar a la función
calcular_area_rectangulo()
