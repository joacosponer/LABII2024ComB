class VistaMascota:

    def mostrar(self, lista):
        print("¡¡mascotas!!")
        for i in lista:
            print(i)

    def registrar(self):
        print("ingrese los datos que se le soliciten")
        nombre = input("nombre:")
        fecha_nac = input("fecha nacimiento:")
        raza = input("raza:")
        propietario = int(input("codigo del propietario"))
        estado = 1
        codigo = input("codigo")
        print("¡¡¡nuevo mascota registrado con exito!!!")
        return nombre,fecha_nac,raza,propietario,estado,codigo

    def codigo_mascota(self):
        codigo = input("ingrese el codigo de la mascota que quiere cambiar su estado")
        return codigo

    def estado_mascota(self):
        estado = input("ingrese el estado al que quiere cambiar. [1]habilitar - [2]deshabilitar")
        return estado

    def mostrar_estado(self, estado):
        print(estado)

    def opciones(self):
        print("[1] mostrar mascotas - [2] registrar nueva mascota - [3] modificar estado")

    def elegir_opcion(self):
        self.opciones()
        opcion = int(input("ingrese una opcion"))
        return opcion

    def seguir_trabajando(self):
        opcion = input("quiere seguir trabajando con las mascotas? [si] [no]".lower())
        return opcion

    def mostrar_mensaje(self, mensaje):
        print(mensaje)
