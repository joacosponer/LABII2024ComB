class VistaConsulta:

    def mostrar(self, lista):
        for consulta in lista:
            print(consulta)

    def codigo_mascota(self):
        codigo = input("ingrese el codigo de la mascota")
        return codigo

    def registrar_fecha(self):
        fecha = input("ingrese la fecha de la consulta xx/xx/xxxx")
        return fecha

    def registrar_vet(self):
        veterinario = input("ingrese el codigo del veterinario que hizo la consulta")
        return veterinario

    def registrar_diagnostico(self):
        diagnostico = input("ingrese el codigo del diagnostico que se le hizo")
        return diagnostico

    def registrar_vacuna(self):
        vacuna = input("ingrese el codigo de la vacuna que se le coloco.\nsi la vacuna no esta registrada ingerese [0]")
        return vacuna

    def registrar_fichamedica(self):
        fichamedica = input("ingrese el codigo de la mascota a la que se le hizo la consulta")
        return fichamedica

    def mostrar_vacunas(self, vacuna):
        print("vacunas ya registradas")
        print(vacuna)

    def mostrar_veterinarios(self, veterinario):
        print("veterinarios ya registrados")
        print(veterinario)

    def opciones_fichamedica(self):
        print("[1] conocer ficha medica")

    def opciones_consulta(self):
        print("[1] registrar consulta - [2] calcular cantidad x mascota")

    def elegir_opcion(self):
        opcion = int(input("ingrese una opcion"))
        return opcion

    def seguir_trabajando(self):
        opcion = input("quiere seguir trabajando con las fichas medicas? [si] [no]".lower())
        return opcion

    def mostrar_mensaje(self, mensaje):
        print(mensaje)