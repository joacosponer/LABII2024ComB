class VistaRaza:

    def registrar(self):
        print("ingrese los datos que se le pidan")
        codigo = input("codigo:")
        nombre = input("nombre de la raza:")
        especie = input("especie:")
        estado = 1
        return codigo,nombre,especie,estado

    def mostrar(self, lista):
        print("!!!razas¡¡¡")
        for i in lista:
            print(i)

    def opciones(self):
        print("[1] mostrar razas [2] registrar nueva raza")

    def elegir_opcion(self):
        self.opciones()
        opcion = int(input("ingrese una opcion"))
        return opcion

    def seguir_trabajando(self):
        opcion = input("quiere seguir trabajando con las mascotas? [si] [no]".lower())
        return opcion

    def mostrar_mensaje(self, mensaje):
        print(mensaje)