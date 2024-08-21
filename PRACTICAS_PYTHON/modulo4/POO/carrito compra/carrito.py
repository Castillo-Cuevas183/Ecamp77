from producto import StockInsuficienteError

class Carrito:
    def __init__(self):
        self.__productos = {}

    def agregar_producto(self, producto, cantidad):
        if cantidad > producto.cantidad_en_stock:
            raise StockInsuficienteError(f"No hay suficiente stock para {producto.nombre}. Stock disponible: {producto.cantidad_en_stock}")
        
        if producto.nombre in self.__productos:
            self.__productos[producto.nombre]['cantidad'] += cantidad
        else:
            self.__productos[producto.nombre] = {
                'producto': producto,
                'cantidad': cantidad
            }
        # Actualizar el stock del producto
        producto.cantidad_en_stock -= cantidad

    def eliminar_producto(self, nombre_producto):
        if nombre_producto in self.__productos:
            producto = self.__productos[nombre_producto]['producto']
            cantidad = self.__productos[nombre_producto]['cantidad']
            producto.cantidad_en_stock += cantidad  # Devolver la cantidad al stock
            del self.__productos[nombre_producto]
        else:
            print(f"El producto {nombre_producto} no está en el carrito.")

    def calcular_total(self):
        total = 0
        for item in self.__productos.values():
            total += item['producto'].precio * item['cantidad']
        return total

    def mostrar_carrito(self):
        if not self.__productos:
            print("El carrito está vacío.")
        else:
            print("Productos en el carrito:")
            for nombre, item in self.__productos.items():
                producto = item['producto']
                cantidad = item['cantidad']
                print(f"{nombre}: {cantidad} unidad(es) a ${producto.precio:.2f} cada una.")


