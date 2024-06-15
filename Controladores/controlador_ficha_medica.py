from Vistas.vista_ficha_medica import VistaFichaMedica
from Modelos.fichaMedica import FichaMedica
from Controladores.controlador_mascota import ControladorMascota


class ControladorFichaMedica:

    def __init__(self, mascota=ControladorMascota(), vista=VistaFichaMedica()):
        self.vista = vista
        self.controlador_mascota = mascota
        self.lista_fichaMedica = []

    def cargar_fichaMedia(self):
        self.controlador_mascota.cargar_mascotas()
        with open("Recursos/fichaMedica.txt") as file:
            lineas = file.readlines()
        for linea in lineas:
            datos = linea.strip().split(",")
            obj_mascota = self.controlador_mascota.buscar_mascota(datos[1])
            self.lista_fichaMedica.append(FichaMedica(datos[0], obj_mascota, datos[2]))

    def registrar_fichaMedica(self):
        pass

    def mostrar_fichaMedica(self):
        self.vista.mostrar(self.lista_fichaMedica)

    def buscar_fichaMedica(self, codigo):
        for fichaMedica in self.lista_fichaMedica:
            if fichaMedica.codigo == codigo:
                return fichaMedica

    def menu_fichaMedica(self):
        while True:
            opcion = self.vista.elegir_opcion()
            if opcion == 1:
                self.mostrar_fichaMedica()
            if self.vista.seguir_trabajando() == "no":
                break
        self.vista.mostrar_mensaje(mensaje="gestion de fichas medicas terminada!!!")
