class VistaVacuna:

    def mostrar(self, lista):
        print("¡¡vacunas!!")
        for i in lista:
            print(i)
            
    def registrar(self):
        print("ingrese las opciones que se le pidan")
        nombre = input("nombre:")
        tipo_vacuna = input("tipo vacuna:")
        estado = 1
        codigo = input("codigo:")
        return nombre,tipo_vacuna,estado,codigo

    def codigo_vacuna(self):
        codigo = input("ingrese el codigo de la vacuna que quiere cambiar su estado")
        return codigo

    def estado_vacuna(self):
        estado = input("ingrese el estado al que quiere cambiar. [1]habilitar - [2]deshabilitar")
        return estado

    def mostrar_estado(self, estado):
        print(estado)

    def opciones(self):
        print("[1] mostrar vacunas - [2] registrar nueva vacunas - [3] modificar estado")

    def elegir_opcion(self):
        self.opciones()
        opcion = int(input("ingrese una opcion"))
        return opcion

    def seguir_trabajando(self):
        opcion = input("quiere seguir trabajando con las mascotas? [si] [no]".lower())
        return opcion

    def mostrar_mensaje(self, mensaje):
        print(mensaje)