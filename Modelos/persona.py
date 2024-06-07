class Persona:

    def __init__(self, nombre, direccion, mail, dni, codigo, estado):
        self.nombre = nombre
        self.direccion = direccion
        self.mail = mail
        self.DNI = dni
        self.codigo = codigo
        self.estado = estado

    def __str__(self):
        return f"nombre: {self.nombre}"

    def __repr__(self):
        return f"nombre: {self.nombre}"

    def get_estado(self):
        return f"codigo: {self.codigo} - {self.nombre} - estado: {self.estado}"

    def habilitar(self):
        self.estado = 1

    def deshabilitar(self):
        self.estado = 0


class Propietario(Persona):

    def __init__(self, nombre, direccion, mail, dni, codigo, estado):
        super().__init__(nombre, direccion, mail, dni, codigo, estado)




class Veterinario(Persona):

    def __init__(self, nombre, direccion, mail, dni, codigo, estado, especialidad):
        super().__init__(nombre, direccion, mail, dni, codigo, estado)
        self.especialidad = especialidad

    def __str__(self):
        return f"nombre: {self.nombre}, especialidad: {self.especialidad}"

    def __repr__(self):
        return f"nombre: {self.nombre}, especialidad: {self.especialidad}"



