from Modelos import persona
from Modelos.vacuna import Vacuna
from Modelos.mascota import Mascota
from Modelos.raza import Raza
from Controladores.controlador_menu import ControladorMenu

lista_propietarios = []
lista_veterinarios = []
lista_vacunas = []
lista_mascotas = []
lista_raza = []



def cargar_propietarios():
    with open("Recursos/propietarios.txt") as file:
        renglones = file.readlines()
    for renglon in renglones:
        datos = renglon.strip().split(",")
        lista_propietarios.append(persona.Propietario(datos[0], datos[1], datos[2], datos[3], datos[4], datos[5]))


def cargar_veterinarios():
    with open("Recursos/veterinarios.txt") as file:
        renglones = file.readlines()

        for renglon in renglones:
            datos = renglon.strip().split(",")
            lista_veterinarios.append(
                persona.Veterinario(datos[0], datos[1], datos[2], datos[3], datos[4], datos[5], datos[6]))

    for renglon in renglones:
        datos = renglon.strip().split(",")
        lista_veterinarios.append(
            persona.Veterinario(datos[0], datos[1], datos[2], datos[3], datos[4], datos[5], datos[6]))



def cargar_Vacuna():
    with open("Recursos/vacuna.txt") as file:
        lineas=file.readlines()
    for linea in lineas:
        datos = linea.strip().split(",")
        lista_vacunas.append(Vacuna(datos[0], datos[1], datos[2], datos[3]))


def cargar_mascotas():
    with open("Recursos/mascotas.txt") as file:
        lineas = file.readlines()
    for linea in lineas:
        datos = linea.strip().split(",")
        obj_raza = buscar_raza(datos[4])
        lista_mascotas.append(Mascota(datos[0], datos[1], datos[2], datos[3], obj_raza))


def cargar_raza():
    with open("Recursos/raza.txt") as file:
        lineas = file.readlines()
    for linea in lineas:
        datos = linea.strip().split(",")
        lista_raza.append(Raza(datos[0], datos[1], datos[2], datos[3]))


def buscar_raza(codigo):
    for raza in lista_raza:
        if raza.codigo == codigo:
            return raza




def main():
    controlador_menu = ControladorMenu()
    controlador_menu.menu()
    """
    cargar_propietarios()
    cargar_veterinarios()
    cargar_Vacuna()
    cargar_raza()
    cargar_mascotas()
    print(lista_propietarios)
    print(lista_veterinarios)
    print(lista_vacunas)
    print(lista_raza)
    print(lista_mascotas)"""






if __name__ == '__main__':
    main()
