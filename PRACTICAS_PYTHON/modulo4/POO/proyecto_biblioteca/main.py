from libro import Libro
from revista import Revista
from periodico import Periodico

def main():
    libro = Libro("El Hobbit", "J.R.R. Tolkien", 1937, 310)
    revista = Revista("National Geographic", "Varios", 2023, 800)
    periodico = Periodico("El País", "Varios", 2024, "15-08-2024")
    
    print(libro.informacion())
    print(revista.informacion())
    print(periodico.informacion())

if __name__ == "__main__":
    main()
