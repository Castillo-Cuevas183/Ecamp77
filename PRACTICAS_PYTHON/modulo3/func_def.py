

def sin_retorno():
    print("Esta funcion no tiene retorno.")#metodo sin retorno

def retorno_unico(a,b):
    return a + b #retorno unico

def retorno_multiple(a,b,c):
    return a,b,c #retorno multiple
    


#Main
sin_retorno()
#invocar retorno unico
x=5
y=20
retorno2=retorno_unico(x,y)
print(f"el retorno unico: {retorno2}")
retorno3=retorno_unico(90,100)
print(f"el retorno unico: {retorno3}")

#invocar retorno multiple
x,y,z = retorno_multiple(7,8,9)
print(f"el retorno multiple: {x}, {y}, {z}")

