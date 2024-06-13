class VistaDiagnostico:

    def registrar(self):
        print("ingrese los datos que se le pidan")
        descripcion = input("descripcion:")
        estado = 1
        print("¡¡¡nuevo diagnostico registrado con exito!!!")
        return descripcion,estado

    def opciones(self):
        print("[1] registrar diagnosticos")

    def elegir_opcion(self):
        self.opciones()
        opcion = int(input("ingrese una opcion"))
        return opcion

    def seguir_trabajando(self):
        opcion = input("quiere seguir trabajando con las mascotas? [si] [no]".lower())
        return opcion

    def mostrar_mensaje(self, mensaje):
        print(mensaje)
