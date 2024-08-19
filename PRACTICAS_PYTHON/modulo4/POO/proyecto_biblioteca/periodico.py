from materialbiblioteca import MaterialBiblioteca

class Periodico(MaterialBiblioteca):
    def __init__(self, titulo, autor, año_publicacion, fecha):
        super().__init__(titulo, autor, año_publicacion)
        self.fecha = fecha
    
    def informacion(self):
        info_base = super().informacion()
        return f"{info_base}, Fecha: {self.fecha}"
