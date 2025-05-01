try:
    print("Menú de operaciones:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    opcion = int(input("Seleccione una opción (1-4): "))

    if opcion >= 1 and opcion <= 4:
        numero1 = float(input("Ingrese el primer número: "))
        numero2 = float(input("Ingrese el segundo número: "))

        if opcion == 1:
            print("La suma es:", numero1 + numero2)
        elif opcion == 2:
            print("La resta es:", numero1 - numero2)
        elif opcion == 3:
            print("El producto es:", numero1 * numero2)
        elif opcion == 4:
            if numero2 != 0:
                print("El cociente es:", numero1 / numero2)
            else:
                print("Error: División por cero no permitida, el divisor debe ser mayor a 0")
    else:
        print("Opción no válida. Por favor, seleccione una opción entre 1 y 4.")

except ValueError:
    print("Error: Ingrese un número válido.")
