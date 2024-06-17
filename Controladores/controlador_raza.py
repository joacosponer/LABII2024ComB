from Vistas.vista_raza import VistaRaza
from Modelos.raza import Raza


class ControladorRaza:
    def __init__(self,vista=VistaRaza()):
        self.vista=vista
        self.lista_razas = []

    def cargar_razas(self):
        with open("Recursos/raza.txt") as file:
            lineas = file.readlines()
        for linea in lineas:
            datos = linea.strip().split(",")
            self.lista_razas.append(Raza(datos[0], datos[1], datos[2], datos[3]))

    def registrar_raza(self):
        self.vista.mostrar_mensaje(mensaje="ingrese los datos que se le soliciten")
        codigo = self.generar_codigo()
        nombre = self.vista.registrar_nombre()
        especie = self.vista.registrar_especie()
        estado = 1
        self.vista.mostrar_mensaje(mensaje="¡¡¡raza registrada con exito!!!")
        with open("Recursos/raza.txt", "a") as file:
            file.write(f"\n{codigo},{nombre},{especie},{estado}")
        self.lista_razas.append(Raza(codigo,nombre,especie,estado))

    def buscar_raza(self, codigo):
        for raza in self.lista_razas:
            if raza.codigo == codigo:
                return raza

    def get_lista_razas(self):
        for raza in self.lista_razas:
            return f"{raza.codigo} - {raza.nombre}"

    def mostrar_razas(self):
        self.vista.mostrar(self.lista_razas)

    def generar_codigo(self):
        ultima_raza = self.lista_razas[-1]
        return int(ultima_raza.codigo) + 1

    def menu_raza(self):
        while True:
            opcion = self.vista.elegir_opcion()
            if opcion == 1:
                self.mostrar_razas()
            if opcion == 2:
                self.registrar_raza()
            if self.vista.seguir_trabajando() == "no":
                break
        self.vista.mostrar_mensaje(mensaje="gestion de razas terminada!!!")
