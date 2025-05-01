# Importación de las clases necesarias
from estudiante import Estudiante
from calificacion import Calificacion

# Lista para almacenar los estudiantes registrados
estudiantes = []

# Bucle principal del programa para interactuar con el usuario
while True:
    # Mostrar las opciones disponibles al usuario
    print("1. Registrar Estudiante")
    print("2. Asignar Calificación")
    print("3. Mostrar Información de Estudiante")
    print("4. Mostrar Todos los Estudiantes")
    print("5. Salir")
    
    # Leer la opción seleccionada por el usuario
    opcion = input("Seleccione una opción: ")

    # Opción 1: Registrar un nuevo estudiante
    if opcion == "1":
        # Solicitar datos del estudiante
        nombre = input("Ingrese el nombre del estudiante: ")
        matricula = input("Ingrese la matrícula del estudiante: ")
        carrera = input("Ingrese la carrera del estudiante: ")

        # Crear un objeto Estudiante y agregarlo a la lista de estudiantes
        estudiante = Estudiante(nombre, matricula, carrera)
        estudiantes.append(estudiante)
        print("Estudiante registrado con éxito.")

    # Opción 2: Asignar una calificación a un estudiante
    elif opcion == "2":
        # Solicitar la matrícula del estudiante
        matricula = input("Ingrese la matrícula del estudiante para asignar calificación: ")
        
        # Buscar al estudiante en la lista
        estudiante = None
        for e in estudiantes:
            if e.matricula == matricula:
                estudiante = e
                break

        # Si se encuentra al estudiante, asignar la calificación
        if estudiante:
            materia = input("Ingrese la materia: ")
            nota = float(input("Ingrese la nota (0 a 10): "))
            calificacion = Calificacion(materia, nota)
            estudiante.agregar_calificacion(calificacion)  # Agregar calificación al estudiante
            print("Calificación asignada.")
        else:
            print("Estudiante no encontrado.")

    # Opción 3: Mostrar la información de un estudiante
    elif opcion == "3":
        # Solicitar la matrícula del estudiante
        matricula = input("Ingrese la matrícula del estudiante para mostrar su información: ")
        
        # Buscar al estudiante en la lista
        estudiante = None
        for e in estudiantes:
            if e.matricula == matricula:
                estudiante = e
                break

        # Si se encuentra al estudiante, mostrar su información
        if estudiante:
            print(estudiante.mostrar_informacion())  # Mostrar información del estudiante
        else:
            print("Estudiante no encontrado.")

    # Opción 4: Mostrar todos los estudiantes registrados
    elif opcion == "4":
        # Verificar si hay estudiantes registrados
        if estudiantes:
            # Mostrar la información de cada estudiante en la lista
            for estudiante in estudiantes:
                print(estudiante.mostrar_informacion())
        else:
            print("No hay estudiantes registrados.")

    # Opción 5: Salir del programa
    elif opcion == "5":
        print("Gracias por usar el sistema.")
        break

    # Si el usuario ingresa una opción inválida
    else:
        print("Opción inválida. Intente nuevamente.")
