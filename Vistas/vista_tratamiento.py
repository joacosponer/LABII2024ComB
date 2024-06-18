class VistaTratamiento:

    def mostrar(self, lista):
        for i in lista:
            print(i)

    def registrar_descripcion(self):
        descripcion = input("ingrese una breve descripcion de el tratamiento recetado")
        return descripcion

    def registrar_diagnostico(self):
        codigo = input("ingrese el codiog del diagnostico que se hizo")
        return codigo

    def opciones_tratamiento(self):
        print("[1] mostrar tratamientos - [2] registrar tratamiento - [3] cantidad de tratamientos realizados")

    def elegir_opcion(self):
        opcion = int(input("ingrese una opcion"))
        return opcion

    def seguir_trabajando(self):
        opcion = input("quiere seguir trabajando con los tratamientos? [si] [no]".lower())
        return opcion

    def mostrar_mensaje(self, mensaje):
        print(mensaje)
