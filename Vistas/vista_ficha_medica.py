class VistaFichaMedica:

    def mostrar(self, lista):
        for i in lista:
            print(i)

    def ingresar_codigo(self):
        codigo = input("ingrese el codigo de la mascota que quiere conocer su ficha medica")
        return codigo


    def opciones(self):
        print("[1] mostrar fichas medicas")

    def elegir_opcion(self):
        self.opciones()
        opcion = int(input("ingrese una opcion"))
        return opcion

    def seguir_trabajando(self):
        opcion = input("quiere seguir trabajando con las fichas medicas? [si] [no]".lower())
        return opcion

    def mostrar_mensaje(self, mensaje):
        print(mensaje)