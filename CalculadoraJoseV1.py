print("Calculadora de operaciones básicas.")

num1 = float(input("Ingresa un número: "))
num2 = float(input("Ingresa otro número: "))

opciones = ["suma", "resta", "multiplicacion", "division"]

print("\nOperaciones disponibles:")
for opcion in opciones:
    print(f"- {opcion}")

operacion = input("\nElige una operación: ").lower()

if operacion == "suma":
    print(f"Resultado: {num1 + num2}")

elif operacion == "resta":
    print(f"Resultado: {num1 - num2}")

elif operacion == "multiplicacion":
    print(f"Resultado: {num1 * num2}")

elif operacion == "division":
    if num2 == 0:
        print("Error: no se puede dividir para cero.")
    else:
        print(f"Resultado: {num1 / num2}")

else:
    print("Operación no válida.")
