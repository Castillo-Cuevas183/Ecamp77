class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    def mostrar(self):
        return f"El producto es: {self.nombre} \n-Precio: {self.precio} \n-Cantidad: {self.cantidad}"
    def agregar_stock(self, cantidad):
        self.cantidad += cantidad #a la cantidad de stock inicial se le agregar lo nuevo que llega al stock
        print(f"Se han agregado: {cantidad} unidades de nombre, la cantidad actual es: {self.cantidad}")
        
    def vender(self,cantidad):
        if self.cantidad >= cantidad: # si la cantidad que me piden es mayor al pedido proceda a restar stock
            self.cantidad -= cantidad #se procede a restar stock
            print(f"Se han vendido: {cantidad} unidades de nombre, la cantidad actual es: {self.cantidad}")
        else:
            print("No hay suficiente stock para vender")
            
    def vender(self,cantidad):
        if cantidad > self.cantidad:
            print(f"No hay suficiente stock para vender {self.nombre} unidades de nombre, solo hay {self.cantidad}")
        else:
            self.cantidad -= cantidad
            print(f"Se han vendido: {cantidad} unidades de nombre, la cantidad actual es: {self.cantidad}")
            


#Main
#Agreagar inputs a producto 1
nombre_pr1=input("Ingresa el producto 1")
precio_pr1=int(input("Ingresa el precio del producto 1"))
cantidad_pr1=int(input("Ingresa el cantidad del producto 1"))

producto1 = Producto (nombre_pr1, precio_pr1, cantidad_pr1)
producto2 = Producto("Mesa", 200, 30)

#mostrar los datos  productos



producto1 = Producto("Laptop",1500,10)
producto2 = Producto("Mesa", 200, 30)

#mostrar los datos  productos
print(producto1.mostrar())
print(producto2.mostrar())

#Agregamos 10 y mostramos el producto de la Laptop
producto1.agregar_stock(10)
print(producto1.mostrar())

#vender 15 unidades y mostrar el producto 2
producto2.vender(15)
print(producto2.mostrar())

#vender 20 unidades y mostrar el producto 2
producto2.vender(2)
print(producto2.mostrar())
