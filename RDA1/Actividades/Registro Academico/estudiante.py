class Estudiante:
    def __init__(self, nombre, matricula, carrera):
        self.nombre = nombre
        self.matricula = matricula
        self.carrera = carrera
        self.calificaciones = []

    def agregar_calificacion(self, calificacion):
        self.calificaciones.append(calificacion)

    def mostrar_informacion(self):
        info = "Nombre: " + self.nombre
        info += "Matrícula: " + self.matricula
        info += "Carrera: " + self.carrera
        if self.calificaciones:
            info += "Calificaciones:\n"
            for calificacion in self.calificaciones:
                info += "  - " + calificacion.materia + ": " + str(calificacion.nota)
        else:
            info += "No tiene calificaciones registradas."
        return info
