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
            self.lista_diagnostico.append(Diagnostico(datos[0], datos[1], datos[2]))

    def registrar_diagnostico(self):
        descripcion = self.vista.registrar_descripcion()
        codigo = self.generar_codigo()
        estado = 1
        with open("Recursos/diagnostico.txt", "a") as file:
            file.write(f"\n{descripcion},{codigo},{estado}")
        self.vista.mostrar_mensaje(mensaje=f"el codigo del diagnostico recien creado es {codigo}")
        self.lista_diagnostico.append(Diagnostico(descripcion,codigo,estado))

    def mostrar_diagnosticos(self):
        self.vista.mostrar(self.lista_diagnostico)

    def buscar_diagnostico(self, codigo):
        for diagnostico in self.lista_diagnostico:
            if diagnostico.codigo == codigo:
                return diagnostico

    def generar_codigo(self):
        ultimo_diagnostico = self.lista_diagnostico[-1]
        return int(ultimo_diagnostico.codigo) + 1

    def menu_diagnostico(self):
        while True:
            opcion = self.vista.elegir_opcion()
            if opcion == 1:
                self.mostrar_diagnosticos()
            if self.vista.seguir_trabajando() == "no":
                break
        self.vista.mostrar_mensaje(mensaje="gestion de diagnosticos terminada!!!")
