class Empleado:
    def __init__(self,nombre,salario):
        self.nombre = nombre #publico
        self._departamento = None # Protegido
        self.__salario = salario # Privado
                
    @property
    def salario(self):
        return "esto cofindencial contacte a RH"
    
    @salario.setter
    def salario(self,nuevo_salario):
        if nuevo_salario > 0:
            self.__salario = nuevo_salario
        else:
            print("Salario debe ser positivo") 
            
    def _asignar_departamento(self,departamento):
        self.departamento = departamento
    
    def _calcular_bonus(self): 
        return self.__salario * 0.1         
#Main
empleado = Empleado("Roberto", 200 ) 
print(empleado.nombre) # Acceso directo a un atributo publico
empleado.salario= 550 #uso de setter
print(empleado.salario) # uso de getter
empleado._asignar_departamento("Ventas") #uso metodo protegido
print("yo soy de RH")
print(empleado._Empleado__salario) 
# empleado._calcular_bonus()


