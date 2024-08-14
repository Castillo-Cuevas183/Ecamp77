frutas=["manzana","banana","cereza"]
if "manzana" in frutas:
    print(" la manzana si estan")
#recorriendo un cadena de texto   
mensaje ="Hola desde Mexico con Tormenta Tropical"
if "Mexico" in  mensaje:
    print("si esta la palabra Mexico")
    
  #tupla  
numeros = (1, 2, 3, 4, 5)
if 3 in numeros:
    print("El número 3 está en la tupla.")
    
 #cojuntos   
colores = {"rojo", "verde", "azul"}
if "verde" in colores:
    print("El color verde está en el conjunto.")

estudiante = {"nombre":"roberto","edad":20}   
#Diccionario
if "edad" in estudiante:
    print("La clave 'edad' está en el diccionario.")
    
# Comprobación Negativa
nombres = ["Ana", "Luis", "Carlos"]
if "Juan" not in nombres:
    print("Juan no está en la lista.")   

# Uso en Bucles
for letra in "python":
    if letra in "aeiou":
        print(f"{letra} es una vocal.")  
      
