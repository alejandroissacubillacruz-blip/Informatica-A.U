print("Calculadora de operaciones básicas.")
num1 = int(input("Ingresa un número: "))
num2 = int(input("Ingresa otro número: "))
opciones = ["suma", "resta", "multiplicacion", "division"]
print("Operaciones disponibles:")
for opcion in opciones:
    print(f"- {opcion}")
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
print(f"\nSuma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")