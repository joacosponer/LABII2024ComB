class Diagnostico:
    def __init__(self,descripcion,estado):
        self.descripcion = descripcion
        self.estado = estado

    def __str__(self):
        return f"estado: {self.estado}, descripcion: {self.descripcion}"


    def __repr__(self):
        return f"estado: {self.estado}, descripcion: {self.descripcion}"

