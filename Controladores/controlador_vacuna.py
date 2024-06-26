from Vistas.vista_vacuna import VistaVacuna
from Modelos.vacuna import Vacuna


class ControladorVacuna:
    def __init__(self, vista=VistaVacuna()):
        self.vista = vista
        self.lista_vacunas = []

    def cargar_vacunas(self):
        with open("Recursos/vacuna.txt") as file:
            lineas = file.readlines()
        for linea in lineas:
            datos = linea.strip().split(",")
            self.lista_vacunas.append(Vacuna(datos[0], datos[1], datos[2], datos[3]))

    def registrar_vacuna(self):
        self.vista.mostrar_mensaje(mensaje="ingrese los datos que se le soliciten")
        nombre = self.vista.registrar_nombre()
        tipo_vacuna = self.vista.registrar_tipo()
        estado = 1
        codigo = self.generar_codigo()
        self.vista.mostrar_mensaje(mensaje="¡¡¡vacuna registrada con exito!!!")
        with open("Rcursos/vacuna.txt", "a") as file:
            file.write(f"\n{nombre},{tipo_vacuna},{estado},{codigo}")
        self.lista_vacunas.append(Vacuna(nombre,tipo_vacuna,estado,codigo))

    def devolver_estado(self):
        for vacuna in self.lista_vacunas:
            self.vista.mostrar_estado(vacuna.get_estado())

    def modificar_estado(self):
        self.vista.mostrar_mensaje(mensaje="estado actual de las mascotas")
        self.devolver_estado()
        codigo = self.vista.codigo_vacuna()
        estado = self.vista.estado_vacuna()
        sig_estado = "habilitado" if estado == 1 else "deshabilitado"
        for vacuna in self.lista_vacunas:
            if vacuna.codigo == codigo:
                if estado == 1:
                    vacuna.habilitar()
                elif estado == 0:
                    vacuna.deshabilitar()
                self.vista.mostrar_mensaje(mensaje=f"¡¡el estado de {vacuna.nombre} fue actualizado a {sig_estado}")

    def buscar_vacuna(self, codigo):
        for vacuna in self.lista_vacunas:
            if vacuna.codigo == codigo:
                return vacuna

    def mostrar_vacunas(self):
        self.vista.mostrar(self.lista_vacunas)

    def get_lista_vacunas(self):
        for vacuna in self.lista_vacunas:
            return vacuna.get_vacuna()

    def generar_codigo(self):
        ultima_vacuna = self.lista_vacunas[-1]
        return int(ultima_vacuna.codigo) + 1

    def menu_vacuna(self):
        while True:
            opcion = self.vista.elegir_opcion()
            if opcion == 1:
                self.mostrar_vacunas()
            if opcion == 2:
                self.registrar_vacuna()
            if opcion == 3:
                self.modificar_estado()
            if self.vista.seguir_trabajando() == "no":
                break
        self.vista.mostrar_mensaje(mensaje="gestion de vacunas terminada!!!")




