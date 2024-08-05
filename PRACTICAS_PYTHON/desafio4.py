# Inicializar el diccionario de jugadores y sus puntuaciones
jugadores = {
    "Oscar": 0,
    "Marcos": 0,
    "Jaime": 0
}

# Lista de niveles con sus correspondientes puntuaciones
niveles = ["Fácil", "Medio", "Difícil", "Experto"]
puntos_por_nivel = [10, 20, 30, 50]

# Sistema de bonificación
bonificacion = 20
tiempo_bonificacion = 30

while True:
    # Solicitar nombre del jugador
    nombre_jugador = input("\nIntroduce el nombre del jugador (o 'salir' para terminar): ")

    # Salir del bucle si el usuario ingresa 'salir'
    if nombre_jugador.lower() == "salir":
        break

    # Verificar si el jugador existe en el diccionario
    if nombre_jugador not in jugadores:
        print("Jugador no encontrado. Por favor, ingresa un nombre válido.")
        continue

    # Solicitar nivel completado
    nivel_completado = input("Introduce el nivel completado (Fácil, Medio, Difícil, Experto): ")

    # Verificar si el nivel ingresado es válido
    if nivel_completado not in niveles:
        print("Nivel no válido. Por favor, elige entre Fácil, Medio, Difícil, Experto.")
        continue

    # Solicitar el tiempo que tardó en completar el nivel
    try:
        tiempo = float(input("Introduce el tiempo que tardó en completar el nivel (en segundos): "))
        if tiempo <= 0:
            print("El tiempo debe ser un número positivo.")
            continue
    except ValueError:
        print("Por favor, ingresa un valor numérico válido para el tiempo.")
        continue

    # Obtener la puntuación correspondiente al nivel completado
    indice_nivel = niveles.index(nivel_completado)
    puntos = puntos_por_nivel[indice_nivel]

    # Verificar si aplica la bonificación
    if (nivel_completado == "Difícil" or nivel_completado == "Experto") and tiempo <= tiempo_bonificacion:
        print(f"¡Bonificación de {bonificacion} puntos por completar el nivel en {tiempo} segundos!")
        puntos += bonificacion

    # Actualizar la puntuación del jugador
    jugadores[nombre_jugador] += puntos

    # Mostrar la puntuación actualizada del jugador
    print(f"{nombre_jugador} ha ganado {puntos} puntos. Puntuación total: {jugadores[nombre_jugador]} puntos.")

# Determinar el líder actual del juego
max_puntuacion = max(jugadores.values())
lideres = [jugador for jugador, puntuacion in jugadores.items() if puntuacion == max_puntuacion]

# Mostrar el/los líder/es actual/es
if len(lideres) == 1:
    print(f"\nEl líder actual es {lideres[0]} con {max_puntuacion} puntos.")
else:
    print(f"\nHay un empate entre los jugadores: {', '.join(lideres)} con {max_puntuacion} puntos.")

# Mostrar las puntuaciones actuales de todos los jugadores
print("\nPuntuaciones actuales:")
for jugador, puntuacion in jugadores.items():
    print(f"{jugador}: {puntuacion} puntos")
