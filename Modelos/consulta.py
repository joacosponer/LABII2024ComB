class Consulta:
    def __init__(self, fecha_consulta, veterinario, diagnostico, vacuna, fichamedica, mascota, tratamiento, codigo,
                 estado):
        self.fecha_consulta = fecha_consulta
        self.veterinario = veterinario
        self.diagnostico = diagnostico
        self.vacuna = vacuna
        self.fichamedica = fichamedica
        self.mascota = mascota
        self.tratamiento = tratamiento
        self.codigo = codigo
        self.estado = estado

    def __str__(self):
        return (f"consulta - {self.codigo}\nfecha_consulta: {self.fecha_consulta}"
                f", veterinario: {self.veterinario.nombre}, diagnostico: {self.diagnostico},"
                f" tratamiento :{self.tratamiento.descripcion}")

    def __repr__(self):
        return (f"consulta - {self.codigo}\nfecha_consulta: {self.fecha_consulta}"
                f", veterinario: {self.veterinario.nombre}, diagnostico: {self.diagnostico},"
                f" tratamiento :{self.tratamiento.descripcion}")
