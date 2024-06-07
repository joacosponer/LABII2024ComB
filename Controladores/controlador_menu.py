from Controladores.controlador_persona import ControladorPropietario, ControladorVeterinario
from Vistas.vista_menu import VistaMenu

class ControladorMenu:

    def __init__(self, propietario = ControladorPropietario(), veterinario=ControladorVeterinario(), vista = VistaMenu()):
        self.controlador_propietario = propietario
        self.controlador_veterinario = veterinario
        self.vista = vista

    def menu(self):
        self.controlador_propietario.cargar_propietarios()
        self.controlador_veterinario.cargar_veterinarios()
        self.vista.opciones()
        while True:
            opcion = self.vista.elegir_opcion()
            if opcion == 1:
                self.controlador_propietario.mostrar()
            if opcion == 2:
                self.controlador_propietario.registrar_nuevo()
            if opcion == 3:
                self.controlador_propietario.modificar_estado()
            if opcion == 4:
                self.controlador_veterinario.mostrar()
            if opcion == 5:
                self.controlador_veterinario.registrar_nuevo()
            if opcion == 6:
                self.controlador_veterinario.modificar_estado()
            if self.vista.seguir_trabajando() == "no":
                break
        self.vista.mostrar_mensaje(mensaje="¡¡¡proceso finalizado con exito!!!")

