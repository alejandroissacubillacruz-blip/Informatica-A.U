print("Calculadora de operaciones básicas.")
while True:
    try:
        num1 = int(input("Ingresa un número: "))
        num2 = int(input("Ingresa otro número: "))
        opcion=int(input("escoja: 1)suma, 2)resta, 3)multiplicacion, 4)division: "))
        if opcion == 1:
            suma = num1 + num2
            print(f"{num1} + {num2} = {suma}")
        elif opcion == 2:
            resta = num1 - num2
            print(f"{num1} - {num2} = {resta}")
        elif opcion == 3:
            multiplicacion = num1 * num2
            print(f"{num1} * {num2} = {multiplicacion}")
        elif opcion == 4:
            division = num1 / num2
            print(f"{num1} / {num2} = {division}")
        else:
            print("Opción no válida.")
    except ValueError:
        print("Por favor, ingrese solo valores numéricos.")
    while True:
        continuar = input("¿Desea realizar otra operación? s/n: ")
        if continuar.lower() == "n":
            print("Gracias por usar la calculadora.")
            break
        elif continuar.lower() == "s":
            break
        else:
            print("Opción no válida.")
    if continuar.lower() == "n":
        break