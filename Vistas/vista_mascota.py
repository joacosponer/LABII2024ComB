class VistaMascota:

    def mostrar(self, lista):
        print("¡¡mascotas!!")
        for i in lista:
            print(i)

    def registrar_nombre(self):
        nombre = input("nombre de la mascota:")
        return nombre

    def registrar_fecha_de_nacimiento(self):
        fecha_nac = input("fecha nacimiento:")
        return fecha_nac

    def registrar_raza(self):
        raza = input("codigo de la raza:")
        return raza

    def registrar_propietario(self):
        propietario = int(input("codigo del propietario:"))
        return propietario

    def mostrar_razas(self, raza):
        print("razas ya registrardas")
        print(raza)

    def mostrar_propietarios(self, propietario):
        print("propietarios ya registrados")
        print(propietario)

    def codigo_mascota(self):
        codigo = input("ingrese el codigo de la mascota que quiere cambiar su estado")
        return codigo

    def estado_mascota(self):
        estado = input("ingrese el estado al que quiere cambiar. [1]habilitar - [2]deshabilitar")
        return estado

    def mostrar_estado(self, estado):
        print(estado)

    def opcion_datos(self):
        print("nombre\nfecha de nacimiento\ncodigo del propietario\nestado\ncodigo de la raza")
        opcion = input("ingrese una opcion".lower())
        return opcion

    def set_nombre(self):
        nombre = input("ingrese el nuevo nombre")
        return nombre

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
