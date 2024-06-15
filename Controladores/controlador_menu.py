from Controladores.controlador_persona import ControladorPropietario, ControladorVeterinario
from Controladores.controlador_mascota import ControladorMascota
from Controladores.controlador_vacuna import ControladorVacuna
from Controladores.controlador_diagnostico import ControladorDiagnostico
from Controladores.controlador_raza import ControladorRaza
from Vistas.vista_menu import VistaMenu


class ControladorMenu:

    def __init__(self, propietario=ControladorPropietario(), veterinario=ControladorVeterinario(), mascota=ControladorMascota(), vacuna=ControladorVacuna(), diagnostico=ControladorDiagnostico(), raza = ControladorRaza(),
                 vista=VistaMenu()
                 ):
        self.controlador_propietario = propietario
        self.controlador_veterinario = veterinario
        self.controlador_mascota = mascota
        self.controlador_vacuna = vacuna
        self.controlador_diagnostico = diagnostico
        self.controlador_raza = raza
        self.vista = vista

    def menu(self):
        self.controlador_propietario.cargar_propietarios()
        self.controlador_veterinario.cargar_veterinarios()
        self.controlador_mascota.cargar_mascotas()
        self.controlador_vacuna.cargar_vacunas()
        self.controlador_diagnostico.cargar_diagnostico()
        self.controlador_raza.cargar_razas()
        while True:
            opcion = self.vista.elegir_opcion()
            if opcion == 1:
                self.controlador_propietario.menu_propietario()
            if opcion == 2:
                self.controlador_veterinario.menu_veterinario()
            if opcion == 3:
                self.controlador_mascota.menu_mascota()
            if opcion == 4:
                self.controlador_raza.menu_raza()
            if opcion == 5:
                self.controlador_diagnostico.menu_diagnostico()
            if opcion == 6:
                self.controlador_vacuna.menu_vacuna()
            if self.vista.seguir_trabajando() == "no":
                break
        self.vista.mostrar_mensaje(mensaje="¡¡¡proceso finalizado con exito!!!")
