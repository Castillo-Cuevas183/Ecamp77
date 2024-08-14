#ejemplo if else 
x=int(input("Ingrese un número X: "))
if x > 5:
    print("x es mayor que 5")
else:
    print("x es menor o igual que 5")

#ejemplo if elif else 
y = int(input("Ingrese otro número Y: "))
if y < 10:
    print("y es mayor que 10")
elif y == 10:
    print("y es igual a 10")
elif y < 20:
    print("y es mayor que 10 y es menor que 20")
else:
    print("y es mayor que 20")
    

edad=int(input("Ingrese su edad: "))
if edad < 18:
    print("Debe tener al menos 18 años para registrarse")
elif 18<=edad<=120:
    print("Registo existoso, Bienvenido")
else:
    print("Edad inválida. Por favor Ingresa una edad correcta")
