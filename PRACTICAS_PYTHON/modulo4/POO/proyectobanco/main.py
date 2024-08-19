from cuenta_ahorra import CuentaAhorro

def main():
    cuenta1= CuentaAhorro("Roberto Hernandez",1000)
    print(f"El nombre del titular es {cuenta1.titular}")
    print(f"El saldos es: ${cuenta1.saldo}")
    print(f"La Tasa de interes es: ${cuenta1.tasa_interes * 100}%")
    
    cuenta1.depositar(500)
    cuenta1.retirar(200)
    cuenta1.aplicar_interes()
    
    print(f"El saldos es: ${cuenta1.saldo}")
    
    cuenta2= CuentaAhorro("Cristian", 20, 0.04)
    print(f"El nombre del titular es {cuenta2.titular}")
    print(f"El saldos es: ${cuenta2.saldo}")
    print(f"La Tasa de interes es: ${cuenta2.tasa_interes * 100}%")
    

if __name__ == "__main__":
    main()
