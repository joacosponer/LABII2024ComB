class Consulta:
    def __init__(self, fecha_consulta, veterinario, diagnostico, vacuna, ficha_medica, estado):
        self.fecha_consulta = fecha_consulta
        self.veterinario = veterinario
        self.diagnostico = diagnostico
        self.vacuna = vacuna
        self.ficha_medica = ficha_medica
        self.estado = estado

    def __str__(self):
        return f"consulta= fecha_consulta: {self.fecha_consulta}, veterinario: {self.veterinario}, diagnostico: {self.diagnostico}"

    def __repr__(self):
        return f"consulta= fecha_consulta: {self.fecha_consulta}, veterinario: {self.veterinario}, diagnostico: {self.diagnostico}"
