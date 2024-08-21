class EdainvalidadError(Exception):
    pass
def verificarEdad(edad):
    if edad < 18:
        raise ValueError("La edad debe ser mayor de 18 años.")
    return "Registro completo"

try:
    mensaje= verificarEdad(20)
    print(mensaje)
except ValueError as e:
    print(f"Error{e}")
    

