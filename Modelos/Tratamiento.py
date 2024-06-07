class Tratamiento:
    def __init__(self,diagnostico,estado):
        self.diagnostico=diagnostico
        self.estado=estado

    def __str__(self):
        return f"estado: {self.estado}, descripcion: {self.descripcion}"


    def __repr__(self):
        return f"estado: {self.estado}, descripcion: {self.descripcion}"

