class Mascota:

    def __init__(self, nombre, fecha_nac, propietario, estado, raza):
        self.nombre = nombre
        self.fecha_nac = fecha_nac
        self.propietario = propietario
        self.estado = estado
        self.raza = raza

    def __str__(self):
        return f"mascota= nombre: {self.nombre}, raza: {self.raza}, propietario: {self.propietario}"

    def __repr__(self):
        return f"mascota= nombre: {self.nombre}, raza: {self.raza}, propietario: {self.propietario}"

