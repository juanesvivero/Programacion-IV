a = int(input("Ingrese un número: "))
b = int(input("Ingrese otro número: "))
c = int(input("Ingrese un tercer número: "))

if a > b:
    print("El número mayor es: ", a)
elif b > a:
    print("El número mayor es: ", b)
elif a == b:
    print("Los números son iguales: ", a, " y ", b)
else:
    print("El número mayor es: ", c)
