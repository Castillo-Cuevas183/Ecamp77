import random 

#Genera r un número secreto
numero_secreto= random.randint(1, 10)

#Juego del adivinador
while True:
    #Pide al usuario un número
    numero_usuario=int(input("Adivina un número del 1 al 10: "))
    
    #Compara el número ingresado con el número secreto
    if numero_usuario == numero_secreto:
        print("Felicitaciones, adivinaste el número!")
        break
    elif numero_usuario < numero_secreto:
        print("El número ingresado es menor que el número secreto.")
    else:
        print("El número ingresado es mayor que el número secreto.")