#ejemplos de uso de f-strings
nombre= "Roberto"
edad= 38
print (f"Hola,{nombre}, tienes {edad} años.")

#ejemplo de suma f-string
precio1= 78293
precio2= 98765
print(f"El total es: ${precio1 + precio2:.2f}" )
#if dentro de un print
temperatura = 30
print(f"La temperatura es {"alta" if temperatura > 25 else "baja"}")

#imprimir llaves dentro de un f-string
print(f"Hola, mi nombre es {{'Roberto'}}")

