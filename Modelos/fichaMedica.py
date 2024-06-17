class FichaMedica:
    def __init__(self, descripcion, mascota, estado):
        self.descripcion = descripcion
        self.mascota = mascota
        self.estado = estado

    def __str__(self):
        return f"ficha_medica - descripcion: {self.descripcion}, mascota: {self.mascota.nombre}"

    def __repr__(self):
        return f"ficha_medica - descripcion: {self.descripcion}, mascota: {self.mascota.nombre}"
