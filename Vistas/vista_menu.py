class VistaMenu:

    def opciones(self):
        print("[1] mostrar propietarios - [2] registrar propietario - [3} modificar estado")
        print("[4] mostrar veterinarios - [5] registrar veterinario - [6] modificar estado")

    def elegir_opcion(self):
        opcion = int(input("ingrese una opcion"))
        return opcion

    def seguir_trabajando(self):
        opcion = input("quiere seguir trabajando? [si] [no]".lower())
        return opcion

    def mostrar_mensaje(self, mensaje):
        print(mensaje)
