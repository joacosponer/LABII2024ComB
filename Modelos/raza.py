class Raza:

    def __init__(self, codigo, nombre, especie, estado):
        self.codigo = codigo
        self.nombre = nombre
        self.especie = especie
        self.estado = estado

    def __str__(self):
        return f"estado: {self.estado}, codigo: {self.codigo},nombre: {self.nombre}, especie: {self.especie} "


    def __repr__(self):
        return f"estado: {self.estado}, codigo: {self.codigo},nombre: {self.nombre}, especie: {self.especie} "

