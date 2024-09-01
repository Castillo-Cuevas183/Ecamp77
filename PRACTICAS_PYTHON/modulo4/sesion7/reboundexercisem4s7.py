class EdadInvalidaError(Exception):
    def __init__(self, mensaje="La entrada no es un número entero."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

def solicitar_edad():
    while True:
        try:
            edad = int(input("Ingrese su edad: "))
            return edad
        except ValueError:
            raise EdadInvalidaError()

def verificar_adulto(edad):
    if edad >= 18:
        print("Es adulto.")
    else:
        print("No es un adulto.")

# Ejecución del programa
while True:
    try:
        edad = solicitar_edad()
        verificar_adulto(edad)
        break
    except EdadInvalidaError as e:
        print(e)
        print("Por favor, ingrese un número entero válido.")
