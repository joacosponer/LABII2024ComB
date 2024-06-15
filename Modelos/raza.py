class Raza:

    def __init__(self, codigo, nombre, especie, estado):
        self.codigo = codigo
        self.nombre = nombre
        self.especie = especie
        self.estado = estado

    def __str__(self):
        return f"raza: {self.nombre} - especie a la que pertenece: {self.especie}"

    def __repr__(self):
        return f"raza: {self.nombre} - especie a la que pertenece: {self.especie}"

