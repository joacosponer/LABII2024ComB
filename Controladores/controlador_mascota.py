from Vistas.vista_mascota import VistaMascota
from Modelos.mascota import Mascota
from Controladores.controlador_persona import ControladorPropietario


class ControladorMascota:
    def __init__(self, propietario=ControladorPropietario(), vista=VistaMascota()):
        self.vista = vista
        self.controlador_propietario = propietario
        self.lista_mascotas = []

    def cargar_mascotas(self):
        self.controlador_propietario.cargar_propietarios()
        with open("Recursos/mascotas.txt") as file:
            lineas = file.readlines()
        for linea in lineas:
            datos = linea.strip().split(",")
            obj_propietario = self.controlador_propietario.buscar_propietario(datos[2])
            self.lista_mascotas.append(Mascota(datos[0], datos[1], obj_propietario, datos[3], datos[4], datos[5]))

    def registrar_mascotas(self):
        nombre, fecha_nac, raza, propietario, estado, codigo = self.vista.registrar()
        with open("Recursos/mascotas.txt", "a") as file:
            file.write(f"\n{nombre},{fecha_nac},{raza},{propietario},{estado},{codigo}")
        self.lista_mascotas.append(Mascota(nombre, fecha_nac, raza, propietario, estado, codigo))

    def devolver_estado(self):
        for mascota in self.lista_mascotas:
            self.vista.mostrar_estado(mascota.get_estado())

    def modificar_estado(self):
        self.vista.mostrar_mensaje(mensaje="estado actual de las mascotas")
        self.devolver_estado()
        codigo = self.vista.codigo_mascota()
        estado = self.vista.estado_mascota()
        sig_estado = "habilitado" if estado == 1 else "deshabilitado"
        for mascota in self.lista_mascotas:
            if mascota.codigo == codigo:
                if estado == 1:
                    mascota.habilitar()
                elif estado == 0:
                    mascota.deshabilitar()
                self.vista.mostrar_mensaje(mensaje=f"¡¡el estado de {mascota.nombre} fue actualizado a {sig_estado}")

    def menu_mascota(self):
        while True:
            opcion = self.vista.elegir_opcion()
            if opcion == 1:
                self.mostrar_mascotas()
            if opcion == 2:
                self.registrar_mascotas()
            if opcion == 3:
                self.modificar_estado()
            if self.vista.seguir_trabajando() == "no":
                break
        self.vista.mostrar_mensaje(mensaje="gestion de mascotas terminada!!!")

    def mostrar_mascotas(self):
        self.vista.mostrar(self.lista_mascotas)


