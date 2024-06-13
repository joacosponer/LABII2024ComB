from Modelos.diagnostico import Diagnostico
from Vistas.vista_diagnostico import VistaDiagnostico


class ControladorDiagnostico:
    def __init__(self, vista=VistaDiagnostico()):
        self.vista = vista
        self.lista_diagnostico = []

    def cargar_diagnostico(self):
        with open("Recursos/diagnostico.txt") as file:
            lineas = file.readlines()
        for linea in lineas:
            datos = linea.strip().split(",")
            self.lista_diagnostico.append(Diagnostico(datos[0], datos[1]))

    def registrar_diagnostico(self):
        descripcion, estado = self.vista.registrar()
        with open("Recursos/diagnostico.txt", "a") as file:
            file.write(f"\n{descripcion},{estado}")
        self.lista_diagnostico.append(Diagnostico(descripcion,estado))

    def menu_diagnostico(self):
        while True:
            opcion = self.vista.elegir_opcion()
            if opcion == 1:
                self.registrar_diagnostico()
            if self.vista.seguir_trabajando() == "no":
                break
        self.vista.mostrar_mensaje(mensaje="gestion de mascotas terminada!!!")
