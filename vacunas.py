class Vacunas:
    def __init__(self,nombre,tipo_vacuna,estado,precio):
        self.nombre = nombre
        self.tipo_vacuna = tipo_vacuna
        self.estado = estado
        self.precio = precio

    def __str__(self):
        return self.nombre

    def __repr__(self):
        return self.nombre