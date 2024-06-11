from Vistas.vista_mascota import VistaMascota
from Modelos.mascota import Mascota
from Controladores.controlador_persona import ControladorPropietario


class ControladorMascota:
    def __init__(self, propietario=ControladorPropietario(), view=VistaMascota()):
        self.view = view
        self.controlador_propietario = propietario
        self.lista_mascotas = []

    def cargar_mascotas(self):
        self.controlador_propietario.cargar_propietarios()
        with open("Recursos/mascotas.txt") as file:
            lineas = file.readlines()
        for linea in lineas:
            datos = linea.strip().split(",")
            nombre = datos[0]
            fecha_nac = datos[1]
            raza = datos[2]
            cod_propietario = datos[3]
            estado = datos[4]
            obj_propietario = self.controlador_propietario.buscar_propietario(cod_propietario)
            self.lista_mascotas.append(Mascota(nombre, fecha_nac, raza, obj_propietario, estado))

    def registrar_mascotas(self):
        nombre, fecha_nac, raza, propietario, estado = self.view.registrar()
        with open("Recursos/mascotas.txt", "a") as file:
            file.write(f"\n{nombre},{fecha_nac},{raza},{propietario},{estado}")
        self.lista_mascotas.append(Mascota(nombre, fecha_nac, raza, propietario, estado))

    def devolver_estado(self):
        for mascota in self.lista_mascotas:
            self.view.mostrar_estado(mascota.get_estado())

    def modificar_estado(self):
        self.view.mostrar_mensaje(mensaje="estado actual de las mascotas")
        self.devolver_estado()
        nombre = self.view.nombre_mascota()
        estado = self.view.estado_mascota()
        sig_estado = "habilitado" if estado == 1 else "deshabilitado"
        for mascota in self.lista_mascotas:
            if mascota.nombre == nombre:
                if estado == 1:
                    mascota.habilitar()
                elif estado == 0:
                    mascota.deshabilitar()
                self.view.mostrar_mensaje(mensaje=f"¡¡el estado de {mascota.nombre} fue actualizado a {sig_estado}")

    def menu_mascota(self):
        while True:
            opcion = self.view.elegir_opcion()
            if opcion == 1:
                self.mostrar_mascotas()
            if opcion == 2:
                self.registrar_mascotas()
            if opcion == 3:
                self.modificar_estado()
            if self.view.seguir_trabajando() == "no":
                break
        self.view.mostrar_mensaje(mensaje="gestion de mascotas terminada!!!")

    def mostrar_mascotas(self):
        self.view.mostrar(self.lista_mascotas)


