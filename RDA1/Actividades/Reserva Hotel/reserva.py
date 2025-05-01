class Reserva:
    def __init__(self, cedula_huesped, fecha_entrada, fecha_salida, tipo_habitacion):
        self.cedula_huesped = cedula_huesped
        self.fecha_entrada = fecha_entrada
        self.fecha_salida = fecha_salida
        self.tipo_habitacion = tipo_habitacion

    def __str__(self):
        return "Huésped con cédula: " + self.cedula_huesped + " | Fecha de entrada: " + self.fecha_entrada + \
                " | Fecha de salida: " + self.fecha_salida + " | Tipo de habitación: " + self.tipo_habitacion
