class Mascota:

    def __init__(self, nombre, fecha_nac, propietario, estado, raza):
        self.nombre = nombre
        self.fecha_nac = fecha_nac
        self.propietario = propietario
        self.estado = estado
        self.raza = raza

    def __str__(self):
        return f"nombre: {self.nombre}, raza: {self.raza}, propietario: {self.propietario.get_propietario()}"

    def __repr__(self):
        return f"nombre: {self.nombre}, raza: {self.raza}, propietario: {self.propietario.get_propietario()}"

    def habilitar(self):
        self.estado = 1

    def deshabilitar(self):
        self.estado = 0

    def get_estado(self):
        return f"{self.nombre} - {self.estado}"