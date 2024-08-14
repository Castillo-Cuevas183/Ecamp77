# Título: Sistema de Puntuación Interactivo para un Juego de Niveles

# Descripción:
# Desarrolla un sistema de puntuación interactivo para un juego de niveles utilizando Python.
# El sistema debe cumplir con los siguientes requisitos:

# 1. Utiliza un diccionario para almacenar los jugadores y sus puntuaciones.

# 2. Implementa una lista de niveles (Fácil, Medio, Difícil, Experto)
# y sus correspondientes puntuaciones.

# 3. Recibe información de la consola para simular una ronda de juego:
#    - Pide al usuario que ingrese el nombre del jugador actual.
#    - Solicita el nivel completado por el jugador.
#    - Pregunta por el tiempo que tardó en completar el nivel.

# 4. Valida la entrada del usuario:
#    - Verifica que el jugador exista en el diccionario de jugadores.
#    - Asegúrate de que el nivel ingresado sea válido.
#    - Comprueba que el tiempo ingresado sea un número positivo.

# 5. Actualiza la puntuación del jugador basándote en el nivel completado.

# 6. Incluye un sistema de bonificación: 
# si un jugador completa un nivel Difícil o Experto en 30 segundos o menos, 
# recibe puntos extra.

# 7. Determina el líder actual del juego.
# En caso de empate, muestra todos los jugadores empatados.

# 8. Muestra las puntuaciones actuales de todos los jugadores.

# Restricciones:
# - Utiliza estructuras if-else para la lógica condicional.
# - Emplea operadores lógicos cuando sea necesario.
# - Usa listas y diccionarios para almacenar y manipular datos.
# - Utiliza input() para recibir información del usuario.

# # Lista de niveles con sus respectivos puntos
# niveles = ["Fácil", "Medio", "Difícil", "Experto"]
# puntos_por_nivel = [10, 20, 30, 50]







# Sistema de puntuación interactivo para un juego de niveles

# Diccionario de jugadores con sus puntuaciones iniciales
# Sistema de puntuación interactivo para un juego de niveles

# Diccionario de jugadores con sus puntuaciones iniciales
jugadores = {
    "Alice": 0,
    "Bob": 0,
    "Charlie": 0
}

# Lista de niveles con sus respectivos puntos
niveles = ["Fácil", "Medio", "Difícil", "Experto"]
puntos_por_nivel = [10, 20, 30, 50]

# Recibir información del usuario
jugador_actual = input("Ingrese el nombre del jugador: ")
nivel_completado = input("Ingrese el nivel completado (Fácil/Medio/Difícil/Experto): ")
tiempo_completado = input("Ingrese el tiempo de completado en segundos: ")

# Validación de entradas
es_valido = False
if jugador_actual == "Alice" or jugador_actual == "Bob" or jugador_actual == "Charlie":
    if nivel_completado == "Fácil" or nivel_completado == "Medio" or nivel_completado == "Difícil" or nivel_completado == "Experto":
        if tiempo_completado.isdigit():
            es_valido = True

if es_valido:
    tiempo_completado = int(tiempo_completado)
    indice_nivel = 0
    if nivel_completado == "Fácil":
        indice_nivel = 0
    elif nivel_completado == "Medio":
        indice_nivel = 1
    elif nivel_completado == "Difícil":
        indice_nivel = 2
    elif nivel_completado == "Experto":
        indice_nivel = 3

    puntos_ganados = puntos_por_nivel[indice_nivel]

    # Sistema de bonificación
    if tiempo_completado <= 30 and (nivel_completado == "Difícil" or nivel_completado == "Experto"):
        puntos_ganados += 5

    # Actualización de puntuación
    jugadores[jugador_actual] += puntos_ganados

    # Verificación del líder
    puntuacion_maxima = max(jugadores["Alice"], jugadores["Bob"], jugadores["Charlie"])
    lideres = []
    if jugadores["Alice"] == puntuacion_maxima:
        lideres.append("Alice")
    if jugadores["Bob"] == puntuacion_maxima:
        lideres.append("Bob")
    if jugadores["Charlie"] == puntuacion_maxima:
        lideres.append("Charlie")

    # Resultado
    if len(lideres) == 1:
        print(f"\nEl líder actual es {lideres[0]} con {puntuacion_maxima} puntos.")
    else:
        print(f"\nHay un empate entre {' y '.join(lideres)} con {puntuacion_maxima} puntos cada uno.")

    print("\nPuntuaciones actuales:")
    print(f"Alice: {jugadores['Alice']} puntos")
    print(f"Bob: {jugadores['Bob']} puntos")
    print(f"Charlie: {jugadores['Charlie']} puntos")
else:
    print("\nEntrada no válida. Por favor, verifique los datos ingresados.")
    if not (jugador_actual == "Alice" or jugador_actual == "Bob" or jugador_actual == "Charlie"):
        print("El jugador ingresado no existe.")
    if not (nivel_completado == "Fácil" or nivel_completado == "Medio" or nivel_completado == "Difícil" or nivel_completado == "Experto"):
        print("El nivel ingresado no es válido.")
    if not tiempo_completado.isdigit():
        print("El tiempo debe ser un número entero positivo.")
