#ducktyping
class Pato:
    def volar(self):
        print( "El pato vuela")
    def nadar(self):
        print("El pato nada")

class Persona:
    def volar(self):
        print("La persona vuela en avión")
    def nadar(self):
        print("La persona nada en la piscina")
        
class Pez:
    def volar(self):
        print("El pez vuela en el mar")
    def nadar(self):
        print("El pez nada en el agua")
    
def hacer_volar_y_nadar(objeto):
    objeto.volar()
    objeto.nadar()

lucas= Pato()
roberto= Persona()
nemo= Pez()


hacer_volar_y_nadar(lucas)
hacer_volar_y_nadar(roberto)
hacer_volar_y_nadar(nemo)

