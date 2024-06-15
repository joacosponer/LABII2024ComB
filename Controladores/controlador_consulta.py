from Vistas.vista_consulta import VistaConsulta
from Modelos.consulta import Consulta
from Controladores.controlador_persona import ControladorVeterinario
from Controladores.controlador_diagnostico import ControladorDiagnostico
from Controladores.controlador_vacuna import ControladorVacuna
from Controladores.controlador_ficha_medica import ControladorFichaMedica


class ControladorConsulta:
    def __init__(self, veterinario=ControladorVeterinario(), diagnostico=ControladorDiagnostico(),
                 vacuna=ControladorVacuna(), ficha_medica=ControladorFichaMedica(), vista=VistaConsulta()):
        self.vista = vista
        self.controlador_veterinario = veterinario
        self.controlador_diagnostico = diagnostico
        self.controlador_vacuna = vacuna
        self.controlador_fichaMedica = ficha_medica
        self.lista_consultas = []

    def cragar_consultas(self):
        self.controlador_veterinario.cargar_veterinarios()
        self.controlador_diagnostico.cargar_diagnostico()
        self.controlador_vacuna.cargar_vacunas()
        self.controlador_fichaMedica.cargar_fichaMedica()
        with open("Recursos/consultas.txt") as file:
            lineas = file.readlines()
        for linea in lineas:
            datos = linea.strip().split(",")
            obj_veterinario = self.controlador_veterinario.buscar_veterinario(datos[1])
            obj_diagnostico = self.controlador_diagnostico.buscar_diagnostico(datos[2])
            obj_vacuna = self.controlador_vacuna.buscar_vacuna(datos[3])
            obj_fichaMedica = self.controlador_fichaMedica
            self.lista_consultas.append(Consulta(datos[0], obj_veterinario, obj_diagnostico, obj_vacuna, obj_fichaMedica, datos[5]))
