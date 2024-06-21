from Vistas.vista_ficha_medica import VistaFichaMedica
from Modelos.fichaMedica import FichaMedica


class ControladorFichaMedica:

    def __init__(self, vista=VistaFichaMedica()):
        self.vista = vista
        self.lista_fichamedica = []
        self.lista_consultas = []

    def cargar_fichamedica(self):
        with open("Recursos/fichaMedica.txt") as file:
            lineas = file.readlines()
        for linea in lineas:
            datos = linea.strip().split(",")
            self.lista_fichamedica.append(FichaMedica(datos[0], datos[2], datos[3]))

    def mostrar_fichamedica(self):
        #print(self.lista_consultas)
        self.vista.mostrar(self.lista_fichamedica)

    def buscar_fichamedica(self, codigo):
        for fichaMedica in self.lista_fichamedica:
            if fichaMedica.codigo == codigo:
                return fichaMedica

    def get_codigo_fichamedica(self):
        codigo = self.vista.ingresar_codigo()
        return codigo

    def menu_fichamedica(self):
        while True:
            opcion = self.vista.elegir_opcion()
            if opcion == 1:
                self.mostrar_fichamedica()
            if self.vista.seguir_trabajando() == "no":
                break
        self.vista.mostrar_mensaje(mensaje="gestion de fichas medicas terminada!!!")
