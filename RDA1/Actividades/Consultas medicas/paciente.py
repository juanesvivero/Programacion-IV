class Consulta:
    def __init__(self, fecha, diagnostico, tratamiento):
        self.fecha = fecha
        self.diagnostico = diagnostico
        self.tratamiento = tratamiento

    def mostrar(self):
        print("Fecha: " + str(self.fecha) + " | Diagnóstico: " + str(self.diagnostico) + " | Tratamiento: " + str(self.tratamiento))


class Paciente:
    def __init__(self, nombre, cedula, edad, tipo_sangre):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad
        self.tipo_sangre = tipo_sangre
        self.consultas = []

    def agregar_consulta(self, fecha, diagnostico, tratamiento):
        self.consultas.append(Consulta(fecha, diagnostico, tratamiento))

    def mostrar_info(self):
        print("\nNombre: " + self.nombre)
        print("Cédula: " + self.cedula)
        print("Edad: " + str(self.edad))
        print("Tipo de sangre: " + self.tipo_sangre)
        print("Consultas:")
        if self.consultas:
            for consulta in self.consultas:
                consulta.mostrar()
        else:
            print("  No tiene consultas registradas.")