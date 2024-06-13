class VistaPersona:
    pass


class VistaPropietario:

    def registrar_nuevo_propietario(self):
        print("ingrese los datos que se le soliciten")
        nombre = input("nmbre")
        direccion = input("direccion")
        mail = input("mail")
        dni = input("dni")
        codigo = input("codigo")
        estado = "1"
        print("¡¡¡cliente registrado con exito!!!")
        return nombre, direccion, mail, dni, codigo, estado

    def mostrar_mensaje(self, mensaje):
        print(mensaje)

    def mostrar_estado(self, estado):
        print(estado)

    def codigo_prop(self):
        codigo = input("ingrese el codigo del propietario que quiere cambiar su estado")
        return codigo

    def estado_prop(self):
        estado = input("ingrese el estado al que quiere cambiar. [1]habilitar - [2]deshabilitar")
        return estado

    def mostrar_props(self, lista):
        print("¡¡¡propietarios!!!")
        for i in lista:
            print(i)

    def opciones(self):
        print("[1] mostrar propietarios - [2] registrar propietario - [3} modificar estado")

    def elegir_opcion(self):
        self.opciones()
        opcion = int(input("ingrese una opcion"))
        return opcion

    def seguir_trabajando(self):
        opcion = input("quiere seguir trabajando con propietarios? [si] [no]".lower())
        return opcion

    def mostrar_mensaje(self, mensaje):
        print(mensaje)


class VistaVeterinario:

    def registrar_nuevo_veterinario(self):
        print("ingrese los datos que se le soliciten")
        nombre = input("nmbre")
        direccion = input("direccion")
        mail = input("mail")
        dni = input("dni")
        codigo = input("codigo")
        estado = "1"
        especialidad = input("especialidad")
        num_matricula = input("N° matricula")
        print("¡¡¡nuevo veterinario registrado con exito!!!")
        return nombre, direccion, mail, dni, codigo, estado, especialidad, num_matricula

    def mostrar_mensaje(self, mensaje):
        print(mensaje)

    def mostrar_estado(self, estado):
        print(estado)

    def codigo_veterinario(self):
        codigo = input("ingrese el codigo del veterinario que quiere cambiar su estado")
        return codigo

    def estado_veterinario(self):
        estado = input("ingrese el estado al que quiere cambiar. [1]habilitar - [2]deshabilitar")
        return estado

    def mostrar_veterinarios(self, lista):
        print("¡¡veterinarios!!")
        for i in lista:
            print(i)

    def opciones(self):
        print("[1] mostrar veterinarios - [2] registrar veterinario - [3] modificar estado")

    def elegir_opcion(self):
        self.opciones()
        opcion = int(input("ingrese una opcion"))
        return opcion

    def seguir_trabajando(self):
        opcion = input("quiere seguir trabajando con veterinarios? [si] [no]".lower())
        return opcion

    def mostrar_mensaje(self, mensaje):
        print(mensaje)
