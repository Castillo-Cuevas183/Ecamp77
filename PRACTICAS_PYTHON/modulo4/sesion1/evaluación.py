# Clase base Persona
class Persona:
    def __init__(self, id, nombre, apellidos, edad):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad

    def concentrarse(self):
        print(f"{self.nombre} {self.apellidos} se está concentrando.")
    
    def viajar(self):
        print(f"{self.nombre} {self.apellidos} está viajando.")

# Clase Futbolista que hereda de Persona
class Futbolista(Persona):
    def __init__(self, id, nombre, apellidos, edad, dorsal, demarcacion):
        super().__init__(id, nombre, apellidos, edad)
        self.dorsal = dorsal
        self.demarcacion = demarcacion

    def jugar_partido(self):
        print(f"{self.nombre} {self.apellidos} está jugando un partido.")
    
    def entrenar(self):
        print(f"{self.nombre} {self.apellidos} está entrenando.")


# Clase Entrenador que hereda de Persona
class Entrenador(Persona):
    def __init__(self, id, nombre, apellidos, edad, id_federacion):
        super().__init__(id, nombre, apellidos, edad)
        self.id_federacion = id_federacion
    
    def dirigir_partido(self):
        print(f"{self.nombre} {self.apellidos} está dirigiendo un partido.")
    
    def dirigir_entrenamiento(self):
        print(f"{self.nombre} {self.apellidos} está dirigiendo un entrenamiento.")

# Clase Masajista que hereda de Persona
class Masajista(Persona):
    def __init__(self, id, nombre, apellidos, edad, titulacion, annos_experiencia):
        super().__init__(id, nombre, apellidos, edad)
        self.titulacion = titulacion
        self.annos_experiencia = annos_experiencia
    
    def dar_masajes(self):
        print(f"{self.nombre} {self.apellidos} está dando masajes.")

# Creando instancias de las clases

# Instancia de un Futbolista
futbolista1 = Futbolista(id=1, nombre="Lionel", apellidos="Messi", edad=36, dorsal=10, demarcacion="Delantero")

# Instancia de un Entrenador
entrenador1 = Entrenador(id=2, nombre="Pep", apellidos="Guardiola", edad=53, id_federacion="FED1234")

# Instancia de un Masajista
masajista1 = Masajista(id=3, nombre="Juan", apellidos="Pérez", edad=45, titulacion="Fisioterapeuta", annos_experiencia=20)

# Uso de los métodos

# Futbolista
futbolista1.concentrarse()  # Lionel Messi se está concentrando.
futbolista1.viajar()        # Lionel Messi está viajando.
futbolista1.jugar_partido() # Lionel Messi está jugando un partido.
futbolista1.entrenar()      # Lionel Messi está entrenando.

# Entrenador
entrenador1.concentrarse()        # Pep Guardiola se está concentrando.
entrenador1.viajar()              # Pep Guardiola está viajando.
entrenador1.dirigir_partido()     # Pep Guardiola está dirigiendo un partido.
entrenador1.dirigir_entrenamiento() # Pep Guardiola está dirigiendo un entrenamiento.

# Masajista
masajista1.concentrarse()  # Juan Pérez se está concentrando.
masajista1.viajar()        # Juan Pérez está viajando.
masajista1.dar_masajes()   # Juan Pérez está dando masajes.