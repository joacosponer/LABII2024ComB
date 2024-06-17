class FichaMedica:
    def __init__(self, descripcion, codigo, estado):
        self.descripcion = descripcion
        self.codigo = codigo
        self.estado = estado

    def get_codigo(self):
        return self.codigo