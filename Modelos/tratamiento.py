class Tratamiento:

    def __init__(self, descripcion, codigo, estado):
        self.descripcion = descripcion
        self.codigo = codigo
        self.estado = estado

    def __str__(self):
        return f"tratamiento- {self.codigo}: {self.descripcion}"
    def __repr__(self):
        return f"tratamiento- {self.codigo}: {self.descripcion}"
