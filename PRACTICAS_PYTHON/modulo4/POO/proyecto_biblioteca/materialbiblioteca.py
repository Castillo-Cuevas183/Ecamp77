
class MaterialBiblioteca:
    def __init__(self, titulo, autor, año_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion
    
    @property
    def año_publicacion(self):
        return self._año_publicacion
    
    @año_publicacion.setter
    def año_publicacion(self, valor):
        if valor > 2024:  # Supongamos que el año máximo permitido es 2024
            raise ValueError("El año de publicación no puede ser en el futuro.")
        self._año_publicacion = valor
    
    def informacion(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Año de Publicación: {self.año_publicacion}"
