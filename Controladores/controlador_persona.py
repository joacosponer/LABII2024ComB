from Modelos.persona import Persona, Propietario, Veterinario
from Vistas.vista_persona import VistaVeterinario, VistaPropietario, VistaPersona


class ControladorPersona:
    def __init__(self, vista):
        self.vista = VistaPropietario()


class ControladorPropietario:
    def __init__(self, vista=VistaPropietario()):
        self.vista = vista
        self.lista_propietarios = []

    def cargar_propietarios(self):
        with open("Recursos/propietarios.txt") as file:
            lineas = file.readlines()
        for linea in lineas:
            datos = linea.strip().split(",")
            self.lista_propietarios.append(Propietario(datos[0], datos[1], datos[2], datos[3], datos[4], datos[5]))

    def registrar_nuevo(self):
        nombre, direccion, mail, dni, codigo, estado = self.vista.registrar_nuevo_propietario()
        with open("Recursos/propietarios.txt", "a") as file:
            file.write(f"\n{nombre},{direccion},{mail},{dni},{codigo},{estado}")
        self.lista_propietarios.append(Propietario(nombre, direccion, mail, dni, codigo, estado))

    def buscar_propietario(self, codigo):
        for propietario in self.lista_propietarios:
            if propietario.codigo == codigo:
                return propietario

    def devolver_estado(self):
        for propietario in self.lista_propietarios:
            print(propietario.get_estado())

    def modificar_estado(self):
        self.vista.mostrar_mensaje(mensaje="estado actual de los propietarios")
        self.devolver_estado()
        codigo = self.vista.codigo_prop()
        estado = self.vista.estado_prop()
        sig_estado = "habilitado" if estado == 1 else "deshabilitado"
        for propietario in self.lista_propietarios:
            if propietario.codigo == codigo:
                if estado == 1:
                    propietario.habilitar()
                elif estado == 0:
                    propietario.deshabilitar()
                self.vista.mostrar_mensaje(
                    mensaje=f"¡¡el estado de {propietario.nombre} fue actualizado a {sig_estado}")

    def mostrar(self):
        self.vista.mostrar_props(self.lista_propietarios)


class ControladorVeterinario:
    def __init__(self, vista=VistaVeterinario()):
        self.vista = vista
        self.lista_veterinarios = []

    def cargar_veterinarios(self):
        with open("Recursos/veterinarios.txt") as file:
            renglones = file.readlines()
            for renglon in renglones:
                datos = renglon.strip().split(",")
                self.lista_veterinarios.append(
                    Veterinario(datos[0], datos[1], datos[2], datos[3], datos[4], datos[5], datos[6]))

    def registrar_nuevo(self):
        nombre, direccion, mail, dni, codigo, estado, especialidad = self.vista.registrar_nuevo_veterinario()
        with open("Recursos/veterinarios.txt", "a") as file:
            file.write(f"\n{nombre},{direccion},{mail},{dni},{codigo},{estado},{especialidad}")
        self.lista_veterinarios.append(Veterinario(nombre, direccion, mail, dni, codigo, estado, especialidad))

    def devolver_estado(self):
        for veterinario in self.lista_veterinarios:
            print(veterinario.get_estado())

    def modificar_estado(self):
        self.vista.mostrar_mensaje(mensaje="estado actual de los veterinarios")
        self.devolver_estado()
        codigo = self.vista.codigo_veterinario()
        estado = self.vista.estado_veterinario()
        sig_estado = "habilitado" if estado == 1 else "deshabilitado"
        for veterinario in self.lista_veterinarios:
            if veterinario.codigo == codigo:
                if estado == 1:
                    veterinario.habilitar()
                elif estado == 0:
                    veterinario.deshabilitar()
                self.vista.mostrar_mensaje(
                    mensaje=f"¡¡el estado del veterinario {veterinario.nombre} fue actualizado a {sig_estado}")

    def mostrar(self):
        self.vista.mostrar_veterinarios(self.lista_veterinarios)

