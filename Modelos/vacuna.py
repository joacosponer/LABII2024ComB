class Vacuna:
    def __init__(self,nombre,tipo_vacuna,estado,codigo):
        self.nombre = nombre
        self.tipo_vacuna = tipo_vacuna
        self.estado = estado
        self.codigo = codigo

    def __str__(self):
        return self.nombre

    def __repr__(self):
        return self.nombre

    def get_estado(self):
        return f"codigo: {self.codigo} - {self.nombre} - estado: {self.estado}"

    def habilitar(self):
        self.estado = 1

    def deshabilitar(self):
        self.estado = 0

    def get_vacuna(self):
        return f"{self.nombre} - {self.codigo}"
