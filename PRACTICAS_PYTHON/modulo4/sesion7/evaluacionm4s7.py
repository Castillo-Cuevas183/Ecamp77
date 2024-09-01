class RangoSalarioError(Exception):
    def __init__(self, salario, mensaje="Salario no está definido en el rango (1000 a 2000)"):
        self.salario = salario
        self.mensaje = mensaje
        super().__init__(f"{salario} -> {mensaje}")

def validar_salario(salario):
    if not (1000 <= salario <= 2000):
        raise RangoSalarioError(salario)
    return f"El salario {salario} está dentro del rango permitido."

# Ejemplo de uso
try:
    salario = int(input("Ingrese el salario: "))
    print(validar_salario(salario))
except RangoSalarioError as e:
    print(e)
except ValueError:
    print("El valor ingresado no es un número válido.")
