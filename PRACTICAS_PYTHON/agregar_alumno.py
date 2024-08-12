# Crea un programa en Python que gestione la información de los estudiantes de una escuela.
# El programa debe permitir
    # agregar nuevos estudiantes,
    # mostrar la lista de estudiantes
    #buscar un estudiante por su nombre.
    
# Requisitos
# Funciones (métodos):
# agregar_estudiante(nombre, edad, grado): Agrega un nuevo estudiante a la lista.
# mostrar_estudiantes(): Muestra la lista completa de estudiantes.
# buscar_estudiante(nombre): Busca un estudiante por su nombre y muestra su información.

# Interacción con el Usuario:
# El programa debe mostrar un menú con las opciones:
    # "Agregar estudiante",  
    # "Mostrar estudiantes",  
    # "Buscar estudiante" y   
    # "Salir".
    
# La opción "Agregar estudiante"
    #   debe pedir el nombre,
    #   edad
    #    grado del estudiante.

# La opción "Mostrar estudiantes"
#   debe mostrar la lista completa de estudiantes.
# La opción "Buscar estudiante"
#   debe pedir el nombre del estudiante y mostrar su información si se encuentra en la lista.

#metodos
estudiantes=[]

def agregar_estudiante(nombre, edad, grado):
    estudiante={"nombre":nombre, "edad":edad, "grado":grado}
    estudiantes.append(estudiante)

def mostrar_estudiantes():
    if not estudiantes:  
        print("No hay estudiantes inscritos.")
    else:
        print("Estudiantes inscritos:")
        for estudiante in estudiantes:
            print(f"El Nombre del estudiante: {estudiante['nombre']}, su edad es: {estudiante['edad']}, y su grado es: {estudiante['grado']}")
    
def buscar_estudiante(nombre):
    for estudiante in estudiantes:
        if estudiante["nombre"].lower() == nombre.lower():
            print(f"\n El Nombre del estudiante: {estudiante['nombre']}, su edad es: {estudiante['edad']}, y su grado es: {estudiante['grado']}")
    else:
        print("El estudiante no se encuentra en la lista.")

def mostrar_menu():
    print("bienvenido al sistema de gestión de estudiantes.")
    print("Menú de opciones:")
    print("1. Agregar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Buscar estudiante")
    print("4. Salir")
    
def pedir_infor_alumno():
    nombre = input("Ingrese el nombre del estudiante: ")
    edad = int(input("Ingrese la edad del estudiante: "))
    grado = input("Ingrese el grado del estudiante: ")
    return nombre, edad, grado



def admon_estudiantes():
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Ingrese la opcion deseada: "))
            
            if opcion == 1:
                nombre, edad, grado = pedir_info_alumno()
                agregar_estudiante(nombre, edad, grado)
            elif opcion == 2:
                mostrar_estudiantes()
            elif opcion == 3:
                nombre = input("Ingresa el nombre del alumno a buscar: ")
                buscar_estudiante(nombre)
            elif opcion == 4:
                print("Gracias por usar sistemas 0077")
                break     
            else:
                print("Opción no válida")
        
        except ValueError:
            print("Error: Por favor, ingresa un número válido para la opción.")

#Main 
admin_estudiantes()

