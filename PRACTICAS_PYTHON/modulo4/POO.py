# pass # para declarar que una clase no haga algo.

class Book:
    def __init__(self,title,autor):
        self.title = title
        self.autor = autor


# clase Periodico
class Newspaper:
    def __init__(self, title):
        self.title = title


# clase Revista
class Revista:
    def __init__(self, title):
        self.title = title


# clase Folleto
class Folleto:
    def __init__(self, title):
        self.title = title


# Main

# Creando objeto
book1= Book("100 años de Soledad", "Gabriel García Márquez")
book2= Book("Código limpio", "Robert C. Martin")
periodico= Newspaper("Universal")
periodico2= Newspaper("Times")
revista= Revista("Capital")
folleto= Folleto("Ieee")


# Invocando Objetos de la clase Book
print(book1)
print(book2.title)
print(book1.title)
print(book1.autor)
print(book2.autor)

# invocando objetos de la clase Newspaper
print(periodico.title)
print(periodico2.title)

# invocando la clase Revista
print(revista.title)

# invocando la clase Folleto
print(folleto.title)

