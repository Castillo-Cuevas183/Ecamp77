from producto import Producto
from carritoprofe import Carrito 

try:
    p1=Producto("Laptop",1000,5)
    p2=Producto("Smartphone",50,10)
    p3=Producto("Diadema",150,2)
    carrito=Carrito()
    carrito.agregar_productos(p1,2)
    carrito.agregar_productos(p2,2) #TODO: AGREGAR UNA EXCEPCION, QUE SUME CUANDO AGREGUR NUEVO PRODUCTO
    carrito.agregar_productos(p3,2)
    carrito.mostrar_carrito()
    carrito.eliminar_productos("Smartphone")
    carrito.mostrar_carrito()

except ValueError as e:
    print(f"Error al crear producto: {e}")
