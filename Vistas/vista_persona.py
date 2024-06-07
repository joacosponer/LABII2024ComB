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
        print("¡¡¡nuevo veterinario registrado con exito!!!")
        return nombre, direccion, mail, dni, codigo, estado, especialidad

    def mostrar_mensaje(self, mensaje):
        print(mensaje)

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