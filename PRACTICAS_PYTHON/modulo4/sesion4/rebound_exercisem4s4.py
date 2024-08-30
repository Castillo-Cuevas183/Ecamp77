class Libro:
    pass

# Crear las instancias libro_1 y libro_2
libro_1 = Libro()
libro_2 = Libro()

# Asigna atributos a libro_1
libro_1.autor = 'Dan Brown'
libro_1.titulo = 'Infierno'

# Asigna atributos a libro_2
libro_2.autor = 'Dan Brown'
libro_2.titulo = 'El Código Da Vinci'
libro_2.year_of_publishment = 2003

# Imprimir el diccionario de atributos de cada libro
print(libro_1.__dict__)
print(libro_2.__dict__)
