class Huesped:
    def __init__(self, nombre, cedula, correo):
        self.nombre = nombre
        self.cedula = cedula
        self.correo = correo

    def __str__(self):
        return self.nombre + " | Cédula: " + self.cedula + " | Email: " + self.correo
