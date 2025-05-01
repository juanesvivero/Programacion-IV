# Importación de clases y funciones necesarias
from huesped import Huesped
from reserva import Reserva
from utilidades import validar_nombre, validar_cedula, validar_tipo_habitacion, ya_esta_registrado

# Listas para almacenar los huéspedes y reservas
huespedes = []
reservas = []

# Función para registrar un nuevo huésped
def registrar_huesped():
    print("Registro de Huésped")
    # Solicitar nombre del huésped y validar que sea correcto
    nombre = input("Ingrese el nombre completo: ")
    while not validar_nombre(nombre):
        nombre = input("Nombre no válido. Ingrese el nombre completo: ")

    # Solicitar cédula y validar que sea correcta
    cedula = input("Ingrese la cédula: ")
    while not validar_cedula(cedula):
        cedula = input("Cédula no válida. Ingrese nuevamente: ")
        
    # Verificar si el huésped ya está registrado
    if ya_esta_registrado(cedula, huespedes):
        print("Ya existe un huésped registrado con esa cédula.")
        return
    # Solicitar correo electrónico
    correo = input("Ingrese el correo electrónico: ")

    # Crear un nuevo objeto Huesped y agregarlo a la lista
    huespedes.append(Huesped(nombre, cedula, correo))
    print("El huésped ha sido registrado correctamente.")

# Función para crear una nueva reserva
def crear_reserva():
    print("Crear Reserva")
    # Solicitar cédula del huésped para verificar si está registrado
    cedula = input("Ingrese la cédula del huésped: ")
    if not any(h.cedula == cedula for h in huespedes):
        print("No existe un huésped con esa cédula.")
        return
    
    # Solicitar fechas de entrada y salida
    dia_entrada = input("Ingrese el dia de entrada: ")
    mes_entrada = input("Ingrese el mes de entrada: ")
    anio_entrada = input("Ingrese el anio de entrada: ")
    fecha_entrada = (dia_entrada + "/" + mes_entrada + "/" + anio_entrada)
    
    dia_salida = input("Ingrese el dia de salida: ")
    mes_salida = input("Ingrese el mes de salida: ")
    anio_salida = input("Ingrese el anio de salida: ")
    fecha_salida = (dia_salida + "/" + mes_salida + "/" + anio_salida)
    
    # Solicitar tipo de habitación y validar que sea uno válido
    tipo_habitacion = input("Tipo de habitación (simple / doble / suite): ")
    while not validar_tipo_habitacion(tipo_habitacion):
        tipo_habitacion = input("Tipo de habitación no válido. Intente nuevamente: ")

    # Crear una nueva reserva y agregarla a la lista
    reservas.append(Reserva(cedula, fecha_entrada, fecha_salida, tipo_habitacion))
    print("La reserva ha sido registrada exitosamente.")

# Función para mostrar la lista de huéspedes registrados
def mostrar_huespedes():
    print("Lista de Huéspedes Registrados")
    # Verificar si hay huéspedes registrados
    if not huespedes:
        print("No hay huéspedes registrados.")
        return
    # Mostrar cada huésped registrado
    for h in huespedes:
        print(h)

# Función para mostrar la lista de reservas registradas
def mostrar_reservas():
    print("Lista de Reservas Registradas")
    # Verificar si hay reservas registradas
    if not reservas:
        print("No hay reservas registradas.")
        return
    # Mostrar cada reserva registrada
    for r in reservas:
        print(r)

# Función principal del programa, que presenta el menú
def menu():
    while True:
        # Mostrar el menú de opciones
        print("    Menú Principal    ")
        print("1. Registrar nuevo huésped")
        print("2. Crear una reserva")
        print("3. Mostrar todos los huéspedes")
        print("4. Mostrar todas las reservas")
        print("5. Salir del sistema")

        # Solicitar al usuario que seleccione una opción
        opcion = input("Seleccione una opción (1-5): ")

        # Ejecutar la acción correspondiente según la opción seleccionada
        if opcion == "1":
            registrar_huesped()
        elif opcion == "2":
            crear_reserva()
        elif opcion == "3":
            mostrar_huespedes()
        elif opcion == "4":
            mostrar_reservas()
        elif opcion == "5":
            print("Fin del programa")
            break
        else:
            # Opción no válida
            print("Opción no válida. Intente nuevamente.")

# Punto de entrada del programa, ejecuta el menú
if __name__ == "__main__":
    menu()
