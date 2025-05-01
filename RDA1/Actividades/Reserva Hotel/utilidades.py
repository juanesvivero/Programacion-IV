# Función para validar el nombre del huésped. Devuelve True si el nombre no está vacío o compuesto solo por espacios.
def validar_nombre(nombre):
    return bool(nombre.strip())

# Función para validar la cédula. Verifica que sea un número de 10 dígitos.
def validar_cedula(cedula):
    return cedula.isdigit() and len(cedula) == 10

# Función para validar el tipo de habitación. Acepta solo los tipos "simple", "doble" o "suite".
def validar_tipo_habitacion(tipo):
    return tipo.lower() in ["simple", "doble", "suite"]

# Función para verificar si un huésped ya está registrado en la lista. Compara la cédula.
def ya_esta_registrado(cedula, lista_huespedes):
    return any(huesped.cedula == cedula for huesped in lista_huespedes)

# Función para validar una fecha (día, mes, año). Verifica que los valores sean numéricos y dentro de los rangos válidos.
def validar_fecha(dia, mes, anio):
    if not (dia.isdigit() and mes.isdigit() and anio.isdigit()):
        return False
    dia, mes, anio = int(dia), int(mes), int(anio)
    if mes < 1 or mes > 12:
        return False
    if dia < 1 or dia > 31:
        return False
    return True

# Función para comparar dos fechas. Devuelve True si la segunda fecha es posterior a la primera.
def comparar_fechas(d1, m1, a1, d2, m2, a2):
    f1 = (int(a1), int(m1), int(d1))
    f2 = (int(a2), int(m2), int(d2))  
    return f2 > f1  # Compara las tuplas, lo que permite determinar cuál es más reciente
