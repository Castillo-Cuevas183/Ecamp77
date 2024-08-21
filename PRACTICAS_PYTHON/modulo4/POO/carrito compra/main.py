from carrito import Carrito
from producto import StockInsuficienteError

# Crear productos
producto1 = Producto("Laptop", 1000, 5)
producto2 = Producto("Mouse", 50, 10)
producto3 = Producto("Teclado", 80, 3)

# Crear carrito
mi_carrito = Carrito()

# Agregar productos al carrito
try:
    mi_carrito.agregar_producto(producto1, 2)  # Agrega 2 Laptops
    mi_carrito.agregar_producto(producto2, 5)  # Agrega 5 Mouse
    mi_carrito.agregar_producto(producto3, 4)  # Intentar agregar más de lo que hay en stock (debe lanzar una excepción)
except StockInsuficienteError as e:
    print(e)

# Mostrar el carrito
mi_carrito.mostrar_carrito()

# Calcular el total
total = mi_carrito.calcular_total()
print(f"El total del carrito es: ${total:.2f}")

# Eliminar un producto del carrito
mi_carrito.eliminar_producto("Mouse")

# Mostrar el carrito después de eliminar un producto
mi_carrito.mostrar_carrito()

# Calcular el total nuevamente
total = mi_carrito.calcular_total()
print(f"El total del carrito después de eliminar un producto es: ${total:.2f}")
