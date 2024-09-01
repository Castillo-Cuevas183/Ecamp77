suma = 3000
contador = 0

try:
    resultado = suma / contador
    print(f"Resultado: {resultado}")
except ZeroDivisionError:
    print("División por cero.")
