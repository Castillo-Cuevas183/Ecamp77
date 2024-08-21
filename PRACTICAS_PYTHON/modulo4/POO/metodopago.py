from abc import ABC, abstractmethod

class MetodoPago(ABC):
    @abstractmethod
    def procesar_pago(self, cantidad):
        pass

#clase hija que procesa pago para tarjeta de credito
class PagoTarjetaCredito(MetodoPago):
    def procesar_pago(self, cantidad):
        print(f"Procesando pago con tarjeta de credito, cantidad: {cantidad}")
    def validaNumeroTarjeta(self,numeroTarjeta):
        print(f"Validando numero tarjeta de{numeroTarjeta}")  


#clase hija que procesa pago con Paypal
class PagoPaypal(MetodoPago):
    def procesar_pago(self, cantidad):
        print(f"Procesando pago con Paypal, cantidad: {cantidad}")
    def validanConexionApi(self):
        print(f"Validando conexion con Api")   
        
#clase hija que procesa pago con Criptomoneda
class PagoCriptomoneda(MetodoPago):
    def procesar_pago(self, cantidad):
        print(f"Procesando pago con Criptomoneda, cantidad: {cantidad}")

def realizar_pago(metodo_pago, cantidad):
    metodo_pago.procesar_pago(cantidad)

#MAin
pago1 = PagoTarjetaCredito()
pago2 = PagoPaypal()
pago3 = PagoCriptomoneda()
pago1.validaNumeroTarjeta("212112")
realizar_pago(pago1,100)
realizar_pago(pago2,500)
realizar_pago(pago3,700)