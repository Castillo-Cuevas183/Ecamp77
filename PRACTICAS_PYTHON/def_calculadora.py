# metodos

def sumar(a, b):
    return a+b

def restar(a, b):
    return a-b

def multiplicar(a, b):
    return a*b

def dividir(a, b):
    return a/b
def imprimir_resultado(a,b, resultado):
    print(f"El resultado de la operacion {a} {b} es: {resultado}")
    def solicitar_numeros(num1,num2):
        num1=float(input("ingresa el primer numero: "))
        num2=float(input("ingresa el segundo numero: "))    
        return num1, num2

def calculadora():
    print("---Bienvenido a la Calculadorea 0077---")
    while True:
        print("\n seleccione una operacion")
        print("1.sumar")
        print("2.restar")
        print("3.multiplicar")
        print("4.dividir")
        print("5.salir")
        opcion = int(input("Ingrese su opcion: "))

        if opcion == 1:
            num1 = float(input("Ingrese el primer numero: "))
            num2 = float(input("Ingrese el segundo numero: "))
            resultado = sumar(num1, num2)
            print(f"El resultado de la suma es: {sumar(num1,num2)} es: {resultado}")
        elif opcion == 2:
            num1 = float(input("Ingrese el primer numero: "))
            num2 = float(input("Ingrese el segundo numero: "))
            resultado = restar(num1, num2)
            print(f"El resultado de la resta es: {restar(num1,num2)} es: {resultado}")
        elif opcion == 3:
            num1 = float(input("Ingrese el primer numero: "))
            num2 = float(input("Ingrese el segundo numero: "))
            resultado = multiplicar(num1, num2)
            print(
                f"El resultado de la multiplicacion es: {multiplicar(num1,num2)} es: {resultado}"
            )
        elif opcion == 4:
            num1 = float(input("Ingrese el primer numero: "))
            num2 = float(input("Ingrese el segundo numero: "))
            resultado = dividir(num1, num2)
            if resultado != 0:
                print(
                    f"El resultado de la division es: {dividir(num1,num2)} es: {resultado}"
                )
            else:
                print("Error: No se puede dividir por 0.")
        elif opcion == 5:
            print("Adios!")
            break


# Main
calculadora()

# Ejemplos de uso
