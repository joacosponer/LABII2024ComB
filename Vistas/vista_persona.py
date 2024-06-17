class VistaPersona:
    pass


class VistaPropietario:

    def registrar_nombre(self):
        nombre = input("nombre:")
        return nombre

    def registrar_direccion(self):
        direccion = input("direccion:")
        return direccion

    def registrar_mail(self):
        mail = input("mail:")
        return mail

    def registrar_dni(self):
        dni = input("DNI:")
        return dni

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

    def registrar_nombre(self):
        nombre = input("nombre:")
        return nombre

    def registrar_direccion(self):
        direccion = input("direccion:")
        return direccion

    def registrar_mail(self):
        mail = input("mail:")
        return mail

    def registrar_dni(self):
        dni = input("DNI:")
        return dni

    def registra_especialidad(self):
        especialidad = input("especialidad:")
        return especialidad

    def registrar_num_matricula(self):
        num_matricula = input("numero de matricula")
        return num_matricula


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
