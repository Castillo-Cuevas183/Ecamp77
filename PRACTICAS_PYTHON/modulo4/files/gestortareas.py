# Este código crea un gestor de tareas que permite agregar nuevas tareas al archivo "tareas.txt".

class GestorTareas:
    def __init__(self, archivo_tareas="tareas.txt"):
        self.archivo_tareas = archivo_tareas
    def abrir_archivo(self, archivo):
        
        def anadir_tareas(self,tarea):
            with open(self.archivo_tareas, 'a') as archivo:
                archivo.write(f"{tarea}\n")
        print ("Tarea agregada con éxito")    
    
    def mostrar_tareas():
        pass
    
    def contar_tareas():
        pass
    
    def buscar_y_reemplazar(self, palabra_buscar, palabra_reemplazar):
        pass
    
    def hacer_respaldo(self):
        pass
    
    
def main():
    gestor = GestorTareas()
    while True:
        print("\n ------Menu-----")
        print("1. Agregar una tarea")
        print("2. Mostrar  tarea")
        print("3. Contar número de tareas")
        print("4. Buscar y reemplazar")
        print("5. Hacer respaldo")
        print("6. Salir")
        opcion = int(input ("Elige una opcion"))
        if (opcion == 1):
            tarea = input("Ingrese la tarea: ")
            gestor.anadir_tareas(tarea)
            print("Tarea agregada correctamente")
        elif (opcion == 6):
            print("Saliendo del programa")
        else:
            print("Opcion no valida")

if __name__ == "__main__":
    main ()




