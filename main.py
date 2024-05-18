import persona

lista_propietarios = []
lista_veterinarios = []


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


def main():
    cargar_propietarios()
    cargar_veterinarios()
    print(lista_propietarios)
    print(lista_veterinarios)


if __name__ == '__main__':
    main()
