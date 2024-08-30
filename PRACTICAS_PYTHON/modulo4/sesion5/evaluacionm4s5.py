# Definición de la clase Persona
class Persona:
    def __init__(self, nombre, apellido, anno):
        self.nombre = nombre
        self.apellido = apellido
        self.anno = anno

# Definición de la clase Departamento
class Departamento:
    def __init__(self, nombre_dpto, nombre_corto_dpto):
        self.nombre_dpto = nombre_dpto
        self.nombre_corto_dpto = nombre_corto_dpto

# Definición de la clase Trabajador que hereda de Persona y Departamento
class Trabajador(Persona, Departamento):
    def __init__(self, nombre, apellido, anno, nombre_dpto, nombre_corto_dpto, salario):
        # Inicialización de los atributos de Persona y Departamento
        Persona.__init__(self, nombre, apellido, anno)
        Departamento.__init__(self, nombre_dpto, nombre_corto_dpto)
        # Atributo específico de Trabajador
        self.salario = salario

# Crear una instancia de Trabajador con los datos proporcionados
trabajador = Trabajador(
    nombre="Claudio", 
    apellido="Fernandez", 
    anno=2005, 
    nombre_dpto="Análisis de Riesgo", 
    nombre_corto_dpto="AR", 
    salario=20000
)

# Imprimir el diccionario de atributos del trabajador
print(trabajador.__dict__)

# Verificar la instancia del objeto trabajador
print(f"Es trabajador instancia de Persona: {isinstance(trabajador, Persona)}")
print(f"Es trabajador instancia de Departamento: {isinstance(trabajador, Departamento)}")
print(f"Es trabajador instancia de Trabajador: {isinstance(trabajador, Trabajador)}")
