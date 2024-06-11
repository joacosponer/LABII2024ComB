from Controladores.controlador_persona import ControladorPropietario, ControladorVeterinario
from Controladores.controlador_mascota import ControladorMascota
from Vistas.vista_menu import VistaMenu

class ControladorMenu:

    def __init__(self, propietario=ControladorPropietario(), veterinario=ControladorVeterinario(), mascota=ControladorMascota(), vista=VistaMenu()):
        self.controlador_propietario = propietario
        self.controlador_veterinario = veterinario
        self.controlador_mascota = mascota
        self.vista = vista

    def menu(self):
        self.controlador_propietario.cargar_propietarios()
        self.controlador_veterinario.cargar_veterinarios()
        self.controlador_mascota.cargar_mascotas()
        while True:
            opcion = self.vista.elegir_opcion()
            if opcion == 1:
                self.controlador_propietario.menu_propietario()
            if opcion == 2:
                self.controlador_veterinario.menu_veterinario()
            if opcion == 3:
                self.controlador_mascota.menu_mascota()

            if self.vista.seguir_trabajando() == "no":
                break
        self.vista.mostrar_mensaje(mensaje="¡¡¡proceso finalizado con exito!!!")

