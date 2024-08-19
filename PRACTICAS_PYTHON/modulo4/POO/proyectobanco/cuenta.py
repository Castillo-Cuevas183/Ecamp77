class Cuenta:
    def __init__(self, titular, saldo=0):
        self._titular = titular #atributo protegido
        self._saldo = saldo  #atributo protegido

    @property
    def titular(self):
        return self._titular
    
    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter  #setter sirve para manipular valores de la clase Cuenta
    def saldo(self, cantidad):
        if cantidad < 0:
            print("el saldo no puede ser negativo o cero")
        else:
            self._saldo = cantidad 
    
    def depositar(self, cantidad):
        if cantidad > 0:
            self._saldo += cantidad
            print(f"Se ha depositado {cantidad} en su cuenta, su nuevo saldo es {self._saldo}")
        else:
            print("No se puede depositar una cantidad negativa o cero")
            
    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self._saldo:
            self._saldo -= cantidad
            print(f"Se ha retirado {cantidad} de su cuenta, su nuevo saldo es {self._saldo}")
        else:
            print("No se puede retirar una cantidad negativa o mayor que su saldo")
            