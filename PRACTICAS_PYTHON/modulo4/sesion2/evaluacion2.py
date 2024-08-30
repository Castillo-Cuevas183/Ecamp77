class Persona:
    def __init__(self, nombre, apellidos, sexo, edad, estatura, peso):
        self._nombre = nombre
        self._apellidos = apellidos
        self._sexo = sexo
        self._edad = edad
        self._estatura = estatura
        self._peso = peso

    # Métodos get
    def get_nombre(self):
        return self._nombre
    
    def get_apellidos(self):
        return self._apellidos
    
    def get_sexo(self):
        return self._sexo
    
    def get_edad(self):
        return self._edad
    
    def get_estatura(self):
        return self._estatura
    
    def get_peso(self):
        return self._peso

    # Métodos set
    def set_nombre(self, nombre):
        self._nombre = nombre
    
    def set_apellidos(self, apellidos):
        self._apellidos = apellidos
    
    def set_sexo(self, sexo):
        self._sexo = sexo
    
    def set_edad(self, edad):
        self._edad = edad
    
    def set_estatura(self, estatura):
        self._estatura = estatura
    
    def set_peso(self, peso):
        self._peso = peso

# Creación de los objetos Persona
persona_1 = Persona(nombre="Pedro", apellidos="Vivas", sexo="Masculino", edad=20, estatura=1.78, peso=68)
persona_2 = Persona(nombre="Juan", apellidos="Camargo", sexo="Masculino", edad=18, estatura=1.8, peso=75)

# Modificación de los atributos
persona_1.set_edad(21)
persona_2.set_apellidos("Santiago")

# Mostrar las actualizaciones
print(f"Persona 1: Nombre: {persona_1.get_nombre()}, Apellidos: {persona_1.get_apellidos()}, Edad: {persona_1.get_edad()} años, Estatura: {persona_1.get_estatura()} mts, Peso: {persona_1.get_peso()} Kg.")
print(f"Persona 2: Nombre: {persona_2.get_nombre()}, Apellidos: {persona_2.get_apellidos()}, Edad: {persona_2.get_edad()} años, Estatura: {persona_2.get_estatura()} mts, Peso: {persona_2.get_peso()} Kg.")
