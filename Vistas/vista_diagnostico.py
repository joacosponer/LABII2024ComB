class VistaDiagnostico:

    def mostrar(self, lista):
        print("diagnosticos que se hicieron")
        for i in lista:
            print(i)

    def registrar_descripcion(self):
        descripcion = input("ingrese el diagnostico que se hizo:")
        return descripcion

    def opciones(self):
        print("[1] mostrar diagnosticos")

    def elegir_opcion(self):
        self.opciones()
        opcion = int(input("ingrese una opcion"))
        return opcion

    def seguir_trabajando(self):
        opcion = input("quiere seguir trabajando con las mascotas? [si] [no]".lower())
        return opcion

    def mostrar_mensaje(self, mensaje):
        print(mensaje)
