class Persona:
    def __init__(self, id, nombre, apellido):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido

    def obtener_datos(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Apellido: {self.apellido}"

class Estudiante(Persona):
    def __init__(self, id, nombre, apellido, codigo_alumno, matricula):
        super().__init__(id, nombre, apellido)
        self.codigo_alumno = codigo_alumno
        self.matricula = matricula

    def obtener_datos(self):
        datos_persona = super().obtener_datos()
        return f"{datos_persona}, Código Alumno: {self.codigo_alumno}, Matrícula: {self.matricula}"

# Ejemplo de uso:
persona = Persona(id=1, nombre="Juan", apellido="Pérez")
estudiante = Estudiante(id=2, nombre="María", apellido="González", codigo_alumno="A123", matricula="2024")

print("Datos de la persona:")
print(persona.obtener_datos())
print("\nDatos del estudiante:")
print(estudiante.obtener_datos())
