class VistaMenu:

    def opciones(self):
        print("[1] gestionar propietarios\n[2] gestionar veterinarios\n[3] gestionar mascotas\n[4] gestionar razas\n"
              "[5] gestionar diagnosticos\n[6] gestionar vacunas\n[7] gestionar fichas medicas\n"
              "[8] gestionar consultas\n[9] gestionar tratamientos")

    def elegir_opcion(self):
        self.opciones()
        opcion = int(input("ingrese una opcion"))
        return opcion

    def seguir_trabajando(self):
        opcion = input("quiere seguir trabajando con alguna otra cosa? [si] [no]".lower())
        return opcion

    def mostrar_mensaje(self, mensaje):
        print(mensaje)
