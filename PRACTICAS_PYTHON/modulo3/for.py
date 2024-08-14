#recorriendo una lista de frutas
frutas = ["Platano", "Manzana", "Sandia", "Pera"]
print (frutas)
for fruta in frutas:
    print (f"El nombre de la fruta es: {fruta}")

#recorriendo una palabra
palabra= "Python"
for letra in palabra:
    print(f"esta es una letra de la palabra: {letra.upper( ) }")
    
estudiante ={"Matías":10, "Roberto":7, "Axel":9}
for nombre in estudiante:
    print (nombre)
for nombre, nota in estudiante.items():
    print(f"El nombre es: {nombre} tiene una calificación: {nota}")


#recorriendo números
numeros = [23,76,34,89,90,100]
suma=0
for numero in numeros:
    suma += numero   #suma = numero  + suma
    print(f"la suma de los número es: {suma}")
    media=suma/len(numeros)
    print(f"la media de los número es: {media}")

#sumar valores de un diccionario
ventas = {"Enero": 1000, "Febrero": 1500,"Marzo": 1200}
total_ventas=0
for mes, cantidad in ventas.items():
    total_ventas += cantidad #total_ventas = cantidad + total_ventas
print(f"El total de ventas: {total_ventas}")


numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
pares = []
for number in numbers:
    if number % 2 == 0:
        pares.append(number)
print(f"Numeros pares {pares}")

#usando break para salir del loop cuando se encuentra un número negativo
nums = [10,20,30,-5,50,20]
for num in nums:
    if num <=  0:
        print(f"El número {num} es no es positivo")
        break
else:
    print(f"todos los numeros son positivos")

