# Excepción personalizada 
class StockInsuficienteError(Exception):
    pass

class Producto:
    def __init__(self, nombre, precio, cantidad_en_stock):
        self.__nombre = nombre #atributo privados
        self.__precio = precio #atributo privados
        self.__cantidad_en_stock = cantidad_en_stock #atributo privados

    # Propiedad para obtener y establecer el nombre
    @property
    def nombre(self):
        return self.__nombre

    # Propiedad para obtener y establecer el precio
    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, valor):
        if valor < 0:
            raise ValueError("El precio no puede ser negativo.")
        self.__precio = valor #en el caso que no hay error debe hacer esto

    # Propiedad para obtener y establecer la cantidad en stock
    @property
    def cantidad_en_stock(self):
        return self.__cantidad_en_stock

    @cantidad_en_stock.setter
    def cantidad_en_stock(self, cantidad):
        if cantidad < 0:
            raise ValueError("La cantidad en stock no puede ser negativa.")
        self.__cantidad_en_stock = cantidad

    def reducir_stock(self, cantidad):
        if cantidad > self.__cantidad_en_stock:
            raise ValueError(f"No hay suficiente stock para reducir {cantidad} unidades de {self.nombre}. Stock disponible: {self.__cantidad_en_stock}")
        self.__cantidad_en_stock -= cantidad