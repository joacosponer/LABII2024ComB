import persona
from vacunas import Vacunas
from Consulta import consulta

lista_propietarios = []
lista_veterinarios = []
lista_vacunas = []
lista_consulta = []


def cargar_propietarios():

    with open("propietarios.txt") as file:
        renglones = file.readlines()
        for renglon in renglones:
            datos = renglon.strip().split(",")
            lista_propietarios.append(persona.Propietario(datos[0], datos[1], datos[2], datos[3], datos[4], datos[5]))


def cargar_veterinarios():
    with open("veterinarios.txt") as file:
        renglones = file.readlines()
        for renglon in renglones:
            datos = renglon.strip().split(",")
            lista_veterinarios.append(persona.Veterinario(datos[0], datos[1], datos[2], datos[3], datos[4], datos[5], datos[6]))


def cargar_Vacuna():
    with open("vacuna.txt") as file:
        lineas=file.readlines()
        for linea in lineas:
            datos=linea.strip().split(",")
            lista_vacunas.append(Vacuna(datos[0], datos[1], datos[2], datos[3]))

def cargar_consulta():
    with open("Consulta.txt") as file:
        lineas=file.readlines()
        for linea in lineas:
            datos=linea.strip().split(",")
            lista_consulta.append(consulta(datos[0],datos[2],datos[3]))


def main():
    cargar_propietarios()
    cargar_veterinarios()
    cargar_Vacuna()
    cargar_consulta()
    print(lista_propietarios)
    print(lista_veterinarios)
    print(lista_vacunas)
    print(lista_consulta)



if __name__ == '__main__':
    main()
