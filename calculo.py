print("bienvenido a la calculadora")
while True:
    try:
        a=int(input("ingrese el primer numero: "))
        b=int(input("ingrese el segundo numero: "))
        c=int(input("ingrese la operacion a realizar: 1-suma, 2-resta, 3-multiplicacion, 4-division: "))
        if c==1:
            print(f"{a} + {b} = {a+b}")
        elif c==2:
            print(f"{a} - {b} = {a-b}")
        elif c==3:
            print(f"{a} * {b} = {a*b}")
        elif c==4:
            print(f"{a} / {b} = {a/b}")
        else:
            print("operacion no valida")
    except ValueError:
        print("no ingreses un valor no numerico")
    while True:
        salir=input("desea continuar? s/n: ")
        if salir.lower()=="s":
            break
        elif salir.lower()=="n":
            print("gracias por usar la calculadora")
            break
        else:
            print("opcion no valida")
    if salir.lower()=="n":
        break