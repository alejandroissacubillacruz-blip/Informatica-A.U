def clacificacion(a):
    if a <= 4:
        return "infante"
    elif a <=10:
        return "niño"
    elif a <= 14:
        return "preadolescente"
    elif a <= 24:
        return "adolescente"
    elif a <= 40:
        return "adulto joven"
    elif a <= 60:
        return "adulto intermedio"
    else:
        return "adulto mayor"
edad=int(input("ingrese la edad: "))
if edad < 0:
    edad*=(-1)
print(f"eres {clacificacion(edad)}")