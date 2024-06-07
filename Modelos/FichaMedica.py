class FichaMedica:
    def __init__(self,descripcion,mascota,estado):
        self.descripcion=descripcion
        self.mascota=mascota
        self.estado=estado

    def __str__(self):
        return f"estado: {self.estado}, descripcion: {self.descripcion}, estado: {self.mascota}"

    def __repr__(self):
        return f"estado: {self.estado}, descripcion: {self.descripcion}, estado: {self.mascota}"

