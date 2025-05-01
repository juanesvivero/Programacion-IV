from paciente import Paciente

lista_pacientes = []
TIPOS_SANGRE = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]

def seleccionar_tipo_sangre():
    print("Seleccione el tipo de sangre:")
    for i in range(len(TIPOS_SANGRE)):
        print(f"{i + 1}. {TIPOS_SANGRE[i]}")

    while True:
        try:
            opcion = int(input("Número correspondiente: "))
            if 1 <= opcion <= len(TIPOS_SANGRE):
                return TIPOS_SANGRE[opcion - 1]
            print("Opción fuera de rango.")
        except ValueError:
            print("Entrada inválida. Ingrese un número.")

def solicitar_cedula():
    while True:
        cedula = input("Ingrese la cédula del paciente (10 dígitos): ")
        if cedula.isdigit() and len(cedula) == 10:
            return cedula
        print("Cédula inválida. Debe contener exactamente 10 dígitos numéricos.")

def solicitar_fecha():
    import datetime
    while True:
        fecha = input("Ingrese la fecha (DD/MM/AAAA): ")
        try:
            datetime.datetime.strptime(fecha, "%d/%m/%Y")
            return fecha
        except ValueError:
            print("Formato de fecha inválido. Debe ser DD/MM/AAAA.")

def solicitar_edad():
    while True:
        edad = input("Edad: ")
        if edad.isdigit() and 0 < int(edad) < 130:
            return int(edad)
        print("Edad inválida. Ingrese un número entre 1 y 129.")

def registrar_nuevo_paciente():
    cedula = solicitar_cedula()
    if buscar_paciente_por_cedula(cedula):
        print("Ya existe un paciente registrado con esa cédula.")
        return

    nombre = input("Nombre: ")
    edad = solicitar_edad()
    tipo_sangre = seleccionar_tipo_sangre()

    nuevo_paciente = Paciente(nombre, cedula, edad, tipo_sangre)
    lista_pacientes.append(nuevo_paciente)
    print("Paciente registrado exitosamente.")

def buscar_paciente_por_cedula(cedula):
    for paciente in lista_pacientes:
        if paciente.cedula == cedula:
            return paciente
    return None

def registrar_nueva_consulta():
    cedula = solicitar_cedula()
    paciente = buscar_paciente_por_cedula(cedula)

    if not paciente:
        print("No se encontró ningún paciente con esa cédula.")
        return

    fecha = solicitar_fecha()
    diagnostico = input("Diagnóstico: ")
    tratamiento = input("Tratamiento: ")

    try:
        paciente.agregar_consulta(fecha, diagnostico, tratamiento)
        print("Consulta registrada exitosamente.")
    except Exception as error:
        print("Ocurrió un error al registrar la consulta: " + str(error))

def mostrar_informacion_paciente():
    cedula = solicitar_cedula()
    paciente = buscar_paciente_por_cedula(cedula)

    if paciente:
        paciente.mostrar_info()
    else:
        print("Paciente no encontrado.")

def mostrar_todos_los_pacientes():
    if not lista_pacientes:
        print("No hay pacientes registrados.")
    else:
        for paciente in lista_pacientes:
            paciente.mostrar_info()