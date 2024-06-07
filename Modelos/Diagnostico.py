class Diagnostico:
    def __init__(self,descripcion,estado):
        self.estado=estado
        self.descripcion=descripcion

    def __str__(self):
        return f"estado: {self.estado}, descripcion: {self.descripcion}"


    def __repr__(self):
        return f"estado: {self.estado}, descripcion: {self.descripcion}"

