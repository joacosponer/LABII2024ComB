from Modelos.persona import Propietario, Veterinario
from Vistas.vista_persona import VistaVeterinario, VistaPropietario


class ControladorPersona:
    pass


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

    def registrar_nuevo_propietario(self):
        self.vista.mostrar_mensaje(mensaje="ingrese los datos que se le soliciten")
        nombre = self.vista.registrar_nombre()
        direccion = self.vista.registrar_direccion()
        mail = self.vista.registrar_mail()
        dni = self.vista.registrar_dni()
        codigo = self.generar_codigo()
        estado = 1
        self.vista.mostrar_mensaje(mensaje="¡¡¡cliente registrado con exito!!!")
        with open("Recursos/propietarios.txt", "a") as file:
            file.write(f"\n{nombre},{direccion},{mail},{dni},{codigo},{estado}")
        self.lista_propietarios.append(Propietario(nombre, direccion, mail, dni, codigo, estado))

    def buscar_propietario(self, codigo):
        for propietario in self.lista_propietarios:
            if propietario.codigo == codigo:
                return propietario

    def devolver_estado(self):
        for propietario in self.lista_propietarios:
            self.vista.mostrar_estado(propietario.get_estado())
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

    def get_lista_propietarios(self):
        for propietario in self.lista_propietarios:
            return f"{propietario.codigo} - {propietario.nombre}"

    def mostrar(self):
        self.vista.mostrar_props(self.lista_propietarios)

    def generar_codigo(self):
        ultimo_prpoietario = self.lista_propietarios[-1]
        return int(ultimo_prpoietario.codigo) + 1

    def menu_propietario(self):
        while True:
            opcion = self.vista.elegir_opcion()
            if opcion == 1:
                self.mostrar()
            if opcion == 2:
                self.registrar_nuevo_propietario()
            if opcion == 3:
                self.modificar_estado()
            if self.vista.seguir_trabajando() == "no":
                break
        self.vista.mostrar_mensaje(mensaje="gestion de propietarios terminada!!!")


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
                    Veterinario(datos[0], datos[1], datos[2], datos[3], datos[4], datos[5], datos[6], datos[7]))

    def registrar_nuevo_veterinario(self):
        self.vista.mostrar_mensaje(mensaje="ingrese los datos que se le soliciten")
        nombre = self.vista.registrar_nombre()
        direccion = self.vista.registrar_direccion()
        mail = self.vista.registrar_mail()
        dni = self.vista.registrar_dni()
        codigo = self.generar_codigo()
        estado = 1
        especialidad = self.vista.registra_especialidad()
        num_matricula = self.vista.registrar_num_matricula()
        self.vista.mostrar_mensaje(mensaje="¡¡¡nuevo veterinario registrado con exito!!!")
        with open("Recursos/veterinarios.txt", "a") as file:
            file.write(f"\n{nombre},{direccion},{mail},{dni},{codigo},{estado},{especialidad},{num_matricula}")
        self.lista_veterinarios.append(Veterinario(nombre, direccion, mail, dni, codigo, estado,
                                                   especialidad, num_matricula))

    def devolver_estado(self):
        for veterinario in self.lista_veterinarios:
            self.vista.mostrar_estado(veterinario.get_estado())

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

    def buscar_veterinario(self, codigo):
        for veterinario in self.lista_veterinarios:
            if veterinario.codigo == codigo:
                return veterinario

    def get_lista_veterinarios(self):
        for veterinario in self.lista_veterinarios:
            return veterinario.get_veterinario()

    def generar_codigo(self):
        ultimo_veterinario = self.lista_veterinarios[-1]
        return int(ultimo_veterinario.codigo) + 1

    def menu_veterinario(self):
        while True:
            opcion = self.vista.elegir_opcion()
            if opcion == 1:
                self.mostrar()
            if opcion == 2:
                self.registrar_nuevo_veterinario()
            if opcion == 3:
                self.modificar_estado()
            if self.vista.seguir_trabajando() == "no":
                break
        self.vista.mostrar_mensaje(mensaje="gestion de veterinarios terminada!!!")
