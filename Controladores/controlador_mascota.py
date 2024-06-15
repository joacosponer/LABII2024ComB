from Vistas.vista_mascota import VistaMascota
from Modelos.mascota import Mascota
from Controladores.controlador_persona import ControladorPropietario
from Controladores.controlador_raza import ControladorRaza


class ControladorMascota:
    def __init__(self, propietario=ControladorPropietario(), raza=ControladorRaza(), vista=VistaMascota()):
        self.vista = vista
        self.controlador_propietario = propietario
        self.controlador_raza = raza
        self.lista_mascotas = []

    def cargar_mascotas(self):
        self.controlador_propietario.cargar_propietarios()
        self.controlador_raza.cargar_razas()
        with open("Recursos/mascotas.txt") as file:
            lineas = file.readlines()
        for linea in lineas:
            datos = linea.strip().split(",")
            obj_propietario = self.controlador_propietario.buscar_propietario(datos[2])
            obj_raza = self.controlador_raza.buscar_raza(datos[4])
            self.lista_mascotas.append(Mascota(datos[0], datos[1], obj_propietario, datos[3], obj_raza, datos[5]))

    def mostrar_razas(self):
        self.vista.mostrar_razas(self.controlador_raza.get_lista_razas())

    def mostrar_propietarios(self):
        self.vista.mostrar_propietarios(self.controlador_propietario.get_lista_propietarios())


    def registrar_mascotas(self):
        self.mostrar_propietarios()
        self.mostrar_razas()
        self.vista.mostrar_mensaje(mensaje="ingrese los datos que se le soliciten")
        nombre = self.vista.registrar_nombre()
        fecha_nac = self.vista.registrar_fecha_de_nacimiento()
        raza = self.vista.registrar_raza()
        propietario = self.vista.registrar_propietario()
        estado = 1
        codigo = self.generar_codigo()
        with open("Recursos/mascotas.txt", "a") as file:
            file.write(f"\n{nombre},{fecha_nac},{raza},{propietario},{estado},{codigo}")
        self.lista_mascotas.append(Mascota(nombre, fecha_nac, raza, propietario, estado, codigo))
        self.vista.mostrar_mensaje(mensaje="mascota registrada con exito!!!")

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

    def mostrar_mascotas(self):
        self.vista.mostrar(self.lista_mascotas)

    def buscar_mascota(self, codigo):
        for mascota in self.lista_mascotas:
            if mascota.codigo == codigo:
                return mascota

    def generar_codigo(self):
        ultima_mascota = self.lista_mascotas[-1]
        return int(ultima_mascota.codigo) + 1

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
