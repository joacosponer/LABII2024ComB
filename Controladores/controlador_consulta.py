from Vistas.vista_consulta import VistaConsulta
from Modelos.consulta import Consulta
from Controladores.controlador_persona import ControladorVeterinario
from Controladores.controlador_diagnostico import ControladorDiagnostico
from Controladores.controlador_vacuna import ControladorVacuna
from Controladores.controlador_ficha_medica import ControladorFichaMedica
from Controladores.controlador_mascota import ControladorMascota
from Controladores.controlador_tratamiento import ControladorTratamiento


class ControladorConsulta:
    def __init__(self, veterinario=ControladorVeterinario(), diagnostico=ControladorDiagnostico(),
                 vacuna=ControladorVacuna(), fichamedica=ControladorFichaMedica(), mascota=ControladorMascota(),
                 tratamiento=ControladorTratamiento(), vista=VistaConsulta()):
        self.vista = vista
        self.controlador_veterinario = veterinario
        self.controlador_diagnostico = diagnostico
        self.controlador_vacuna = vacuna
        self.controlador_fichamedica = fichamedica
        self.controlador_mascota = mascota
        self.controlador_tratamiento = tratamiento
        self.lista_consultas = []

    def cargar_consultas(self):
        self.controlador_veterinario.cargar_veterinarios()
        self.controlador_diagnostico.cargar_diagnostico()
        self.controlador_vacuna.cargar_vacunas()
        self.controlador_mascota.cargar_mascotas()
        self.controlador_tratamiento.cargar_tratamientos()
        with open("Recursos/consultas.txt") as file:
            lineas = file.readlines()
        for linea in lineas:
            datos = linea.strip().split(",")
            obj_veterinario = self.controlador_veterinario.buscar_veterinario(datos[1])
            obj_diagnostico = self.controlador_diagnostico.buscar_diagnostico(datos[2])
            obj_vacuna = self.controlador_vacuna.buscar_vacuna(datos[3])
            obj_fichamedica = self.controlador_fichamedica.buscar_fichamedica(datos[4])
            obj_mascota = self.controlador_mascota.buscar_mascota(datos[5])
            obj_tratamiento = self.controlador_tratamiento.buscar_tratamientos(datos[6])
            self.lista_consultas.append(Consulta(datos[0], obj_veterinario, obj_diagnostico, obj_vacuna, obj_fichamedica,
                                                 obj_mascota, obj_tratamiento, datos[7], datos[8]))

    def registrar_consultas(self):
        fecha = self.vista.registrar_fecha()
        self.vista.mostrar_veterinarios(self.controlador_veterinario.get_lista_veterinarios())
        veterinario = self.vista.registrar_vet()
        self.controlador_diagnostico.registrar_diagnostico()
        diagnostico = self.vista.registrar_diagnostico()
        self.vista.mostrar_vacunas(self.controlador_vacuna.get_lista_vacunas())
        vacuna = self.vista.registrar_vacuna()
        self.controlador_mascota.get_lista_mascotas()
        fichamedica = self.vista.registrar_fichamedica()
        mascota = fichamedica
        self.controlador_tratamiento.registrar_tratamientos()
        tratamiento = self.vista.registrar_tratamiento()
        codigo = self.generar_codigo()
        estado = 1
        self.vista.mostrar_mensaje(mensaje="¡¡¡consulta registrada con exito!!!")
        with open("Recursos/consultas.txt", "a") as file:
            file.write(f"\n{fecha},{veterinario},{diagnostico},{vacuna},{fichamedica},{mascota},{tratamiento}"
                       f",{codigo},{estado}")
        self.lista_consultas.append(Consulta(fecha, veterinario, diagnostico, vacuna, fichamedica, mascota, tratamiento,
                                             codigo, estado))

    def mostrar_consultas(self):
        for consulta in self.lista_consultas:
            if consulta.codigo == self.controlador_fichamedica.get_codigo_fichamedica():
                self.vista.mostrar(self.lista_consultas)

    def get_lista_consultas(self):
        for consulta in self.lista_consultas:
            return consulta

    def generar_codigo(self):
        ultima_consulta = self.lista_consultas[-1]
        return int(ultima_consulta.codigo) + 1

    def cantidad_consultas_x_mascota(self):
        codigo = self.vista.codigo_mascota()
        cont_consultas = 0
        mascota = None
        for consulta in self.lista_consultas:
            if consulta.mascota.codigo == codigo:
                mascota = consulta.mascota.nombre
                cont_consultas += 1
        if cont_consultas > 1:
            self.vista.mostrar_mensaje(mensaje=f"a {mascota} se le realizaron {cont_consultas} consultas en esta veterinaria")
        if cont_consultas == 1:
            self.vista.mostrar_mensaje(mensaje=f"a {mascota} se le realizo {cont_consultas} consulta en esta veterinaria")
        if cont_consultas < 1:
            self.vista.mostrar_mensaje(mensaje=f"{mascota} todavia no tiene consultas realizadas en esta veterinaria")

    def menu_fichamedica(self):
        while True:
            self.vista.opciones_fichamedica()
            opcion = self.vista.elegir_opcion()
            if opcion == 1:
                self.mostrar_consultas()
            if self.vista.seguir_trabajando_fichasmedicas() == "no":
                break
        self.vista.mostrar_mensaje(mensaje="gestion de fichas medicas terminada!!!")

    def menu_consulta(self):
        while True:
            self.vista.opciones_consulta()
            opcion = self.vista.elegir_opcion()
            if opcion == 1:
                self.registrar_consultas()
            if opcion == 2:
                self.cantidad_consultas_x_mascota()
            if self.vista.seguir_trabajando_consultas() == "no":
                break
        self.vista.mostrar_mensaje(mensaje="gestion de consultas terminada!!!")
