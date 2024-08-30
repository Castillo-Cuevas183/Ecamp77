# Definición de la clase Persona
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def movimiento(self):
        return f"{self.nombre} está caminando"

# Definición de la subclase Maratonista que hereda de Persona
class Maratonista(Persona):
    def movimiento(self):
        return f"{self.nombre} está trotando"

# Definición de la subclase Ciclista que hereda de Persona
class Ciclista(Persona):
    def movimiento(self):
        return f"{self.nombre} está rodando"

#Main
# Ejemplo de uso:

# se crean  instancias de cada clase
persona = Persona("Juan")
maratonista = Maratonista("Pedro")
ciclista = Ciclista("Laura")

# Imprimir el estado de movimiento de cada objeto
print(persona.movimiento())      # Salida: Juan está caminando
print(maratonista.movimiento())  # Salida: Pedro está trotando
print(ciclista.movimiento())     # Salida: Laura está rodando

# En este caso, cada clase Persona hereda de la clase Persona y tiene un método movimiento que devuelve el mismo mensaje.