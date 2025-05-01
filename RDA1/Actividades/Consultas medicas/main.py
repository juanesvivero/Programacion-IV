from funciones import (
    registrar_nuevo_paciente,
    registrar_nueva_consulta,
    mostrar_informacion_paciente,
    mostrar_todos_los_pacientes
)

def mostrar_menu():
    print("""
===== MENÚ =====
1. Registrar paciente
2. Registrar consulta
3. Ver un paciente
4. Ver todos los pacientes
5. Salir
""")

def main():
    opciones = {
        "1": registrar_nuevo_paciente,
        "2": registrar_nueva_consulta,
        "3": mostrar_informacion_paciente,
        "4": mostrar_todos_los_pacientes
    }

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        if opcion == "5":
            print("Finalizando el programa.")
            break
        if opcion in opciones:
            opciones[opcion]()
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
