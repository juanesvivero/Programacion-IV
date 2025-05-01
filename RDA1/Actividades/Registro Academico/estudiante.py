class Estudiante:
    # Constructor de la clase Estudiante
    def __init__(self, nombre, matricula, carrera):
        # Inicializar los atributos del estudiante
        self.nombre = nombre        # Nombre del estudiante
        self.matricula = matricula  # Matrícula del estudiante
        self.carrera = carrera      # Carrera del estudiante
        self.calificaciones = []    # Lista vacía para almacenar las calificaciones del estudiante

    # Método para agregar una calificación al estudiante
    def agregar_calificacion(self, calificacion):
        self.calificaciones.append(calificacion)  # Añadir la calificación a la lista

    # Método para mostrar la información del estudiante
    def mostrar_informacion(self):
        # Construir una cadena de texto con la información básica del estudiante
        info = "Nombre: " + self.nombre
        info += "Matrícula: " + self.matricula
        info += "Carrera: " + self.carrera
        
        # Verificar si el estudiante tiene calificaciones registradas
        if self.calificaciones:
            info += "\nCalificaciones:\n"
            # Recorrer las calificaciones y agregarlas a la información
            for calificacion in self.calificaciones:
                info += "  - " + calificacion.materia + ": " + str(calificacion.nota) + "\n"
        else:
            # Si no tiene calificaciones, mostrar mensaje adecuado
            info += "No tiene calificaciones registradas."
        
        # Devolver la información completa del estudiante
        return info
