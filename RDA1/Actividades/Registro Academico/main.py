from estudiante import Estudiante
from calificacion import Calificacion

estudiantes = []

while True:
    print("1. Registrar Estudiante")
    print("2. Asignar Calificación")
    print("3. Mostrar Información de Estudiante")
    print("4. Mostrar Todos los Estudiantes")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del estudiante: ")
        matricula = input("Ingrese la matrícula del estudiante: ")
        carrera = input("Ingrese la carrera del estudiante: ")

        estudiante = Estudiante(nombre, matricula, carrera)
        estudiantes.append(estudiante)
        print("Estudiante registrado con éxito.")

    elif opcion == "2":
        matricula = input("Ingrese la matrícula del estudiante para asignar calificación: ")
        estudiante = None
        for e in estudiantes:
            if e.matricula == matricula:
                estudiante = e
                break

        if estudiante:
            materia = input("Ingrese la materia: ")
            nota = float(input("Ingrese la nota (0 a 10): "))
            calificacion = Calificacion(materia, nota)
            estudiante.agregar_calificacion(calificacion)
            print("Calificación asignada.")
        else:
            print("Estudiante no encontrado.")

    elif opcion == "3":
        matricula = input("Ingrese la matrícula del estudiante para mostrar su información: ")
        estudiante = None
        for e in estudiantes:
            if e.matricula == matricula:
                estudiante = e
                break

        if estudiante:
            print(estudiante.mostrar_informacion())
        else:
            print("Estudiante no encontrado.")

    elif opcion == "4":
        if estudiantes:
            for estudiante in estudiantes:
                print(estudiante.mostrar_informacion())
        else:
            print("No hay estudiantes registrados.")

    elif opcion == "5":
        print("Gracias por usar el sistema.")
        break

    else:
        print("Opción inválida. Intente nuevamente.")
