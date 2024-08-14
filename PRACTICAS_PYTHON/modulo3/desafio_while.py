# Desafío: Adivina el Número Secreto
# Objetivo: Implementar un juego en Python donde el usuario debe adivinar un número secreto entre 1 y 100. 
# El programa debe indicar si el número ingresado es mayor o menor al número secreto y continuar preguntando hasta que el usuario lo adivine.

# Instrucciones:
# Generar un número secreto aleatorio entre 1 y 100.
# Pedir al usuario que adivine el número secreto.
# Comparar el número ingresado por el usuario con el número secreto:
# Si el número ingresado es mayor que el número secreto, mostrar el mensaje: "El número secreto es menor. Intenta de nuevo."
# Si el número ingresado es menor que el número secreto, mostrar el mensaje: "El número secreto es mayor. Intenta de nuevo."
# Si el número ingresado es igual al número secreto, mostrar el mensaje: "¡Felicidades! Has adivinado el número secreto." y terminar el juego.
# Continuar pidiendo al usuario que adivine hasta que acierte el número secreto.

import random

# Generar un número secreto aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)

print("¡Bienvenido al juego de Adivina el Número Secreto!")
print("Debes adivinar el número entre 1 y 100.")

while True:
    try:
        intento = int(input("Adivina el número: "))
        
        # Comparar el número ingresado con el número secreto
        if intento > numero_secreto:
            print("El número secreto es menor. Intenta de nuevo.")
        elif intento < numero_secreto:
            print("El número secreto es mayor. Intenta de nuevo.")
        else:
            print("Felicidades! Has adivinado el número secreto.")
            break
    except ValueError:
        print("Por favor, ingresa un número válido.")
    


# Desafío: Adivina el Número Secreto con Máximo de Intentos con ciclo for 

import random

# Generar un número secreto aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)
max_intentos = 10  # Número máximo de intentos

print("¡Bienvenido al juego de Adivina el Número Secreto!")
print(f"Estoy pensando en un número entre 1 y 100. Tienes {max_intentos} intentos para adivinarlo.")

# Usar un bucle for para limitar el número de intentos
for intento in range(max_intentos):
    try:
        adivinanza = int(input(f"Intento {intento + 1}: Adivina el número entre 1 y 100: "))
        
        # Comparar el número ingresado con el número secreto
        if adivinanza > numero_secreto:
            print("El número secreto es menor.")
        elif adivinanza < numero_secreto:
            print("El número secreto es mayor.")
        else:
            print(f"Felicidades! Has adivinado el número secreto en {intento + 1} intento.")
            break  # Salir del bucle si el número es correcto
    except ValueError:
        print("Por favor, ingresa un número válido.")
    # Si el número no fue adivinado, mostrar un mensaje
    else:
        print(f"Lo siento, has agotado tus {max_intentos} intentos. El número secreto era {numero_secreto}.")
