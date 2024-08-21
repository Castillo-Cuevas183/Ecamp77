def solicitar_numero(mensaje):
    while True:
        try:
            numero = float(input(mensaje))
            return numero
        except ValueError:
            print("Por favor, ingresa un número válido.")

def realizar_operacion(a,b,operador):
    try:
        if operador == "+":
            return a + b
        elif operador == "-":
            return a - b
        elif operador == "*":
            return a * b
        elif operador == "/":
            if b == 0:
                raise ZeroDivisionError("No se puede dividir por cero.")
            return a / b
        else:
            raise ValueError("Operador inválido.")
        
    except ValueError as e:
        print(f"Error: {e}")


# Main
num1= solicitar_numero("Introduce el primer número")
num2= solicitar_numero("Introduce el segundo número")

operaciones= input("Introduce el operador a usar +,-, *, /:")

resultados= realizar_operacion(num1, num2, operaciones)

print(f"El resultado de la operación {num1} {operaciones} {num2} es: {resultados}")
