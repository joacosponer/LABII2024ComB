from Vistas.vista_tratamiento import VistaTratamiento
from Modelos.tratamiento import Tratamiento
from Controladores.controlador_diagnostico import ControladorDiagnostico


class ControladorTratamiento:

    def __init__(self, diagnostico=ControladorDiagnostico(), vista=VistaTratamiento()):
        self.vista = vista
        self.controlador_diagnostico = diagnostico
        self.lista_tratamientos = []

    def cargar_tratamientos(self):
        self.controlador_diagnostico.cargar_diagnostico()
        with open("Recursos/tratamientos.txt") as file:
            lineas = file.readlines()
        for linea in lineas:
            datos = linea.strip().split(",")
            self.lista_tratamientos.append(Tratamiento(datos[0], datos[1], datos[2]))

    def registrar_tratamientos(self):
        descripcion = self.vista.registrar_descripcion()
        codigo = self.generar_codigo()
        estado = 1
        with open("Recursos/tratamientos.txt", "a") as file:
            file.write(f"\n{descripcion},{codigo},{estado}")
        self.vista.mostrar_mensaje(mensaje=f"el codigo del tratamiento recien creado es {codigo}")
        self.lista_tratamientos.append(Tratamiento(descripcion, codigo, estado))

    def generar_codigo(self):
        ultimo_tratamiento = self.lista_tratamientos[-1]
        return int(ultimo_tratamiento.codigo) + 1

    def get_lista_tratamientos(self):
        for tratamiento in self.lista_tratamientos:
            return f"{tratamiento.codigo} - {tratamiento.descripcion}"

    def mostrar_tratamientos(self):
        self.vista.mostrar(self.lista_tratamientos)

    def buscar_tratamientos(self, codigo):
        for tratamiento in self.lista_tratamientos:
            if tratamiento.codigo == codigo:
                return tratamiento

    def cantidad_tratamientos(self):
        cont_tratamientos = 0
        for tratamiento in self.lista_tratamientos:
            cont_tratamientos += 1
        if cont_tratamientos > 1:
            self.vista.mostrar_mensaje(mensaje=f"en esta veterinaria se hicieron {cont_tratamientos} tratamientos")
        if cont_tratamientos == 1:
            self.vista.mostrar_mensaje(mensaje=f"en esta veterinaria se hizo {cont_tratamientos} tratamiento")
        if cont_tratamientos < 1:
            self.vista.mostrar_mensaje(mensaje=f"en esta veterinaria todavia no se hicieron tratamientos")
    def menu_tratamiento(self):
        self.vista.opciones_tratamiento()
        while True:
            opcion = self.vista.elegir_opcion()
            if opcion == 1:
                self.mostrar_tratamientos()
            if opcion == 2:
                self.registrar_tratamientos()
            if opcion == 3:
                self.cantidad_tratamientos()
            if self.vista.seguir_trabajando() == "no":
                break
        self.vista.mostrar_mensaje(mensaje="gestion de tratamientos terminada!!!")


