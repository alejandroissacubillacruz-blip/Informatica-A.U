for i in range(3,15,2):
    print(i)
for i in range(3,15):
    print(i)
letra=["A","B","C","B","E,"]
for i in letra:
    print(i)
for i in enumerate(letra):
    print(i)
for i in enumerate(letra,start=1):
    print(i)
palabra="comisaria"
for letra in palabra:
    print(letra)
for letra in palabra:
    print(letra)
estudiante={"nombre":"alejandro","edad":17,"carrera":"informatica"}
for a in estudiante:
    print(a)
for a ,b in estudiante.items():
    print(a,b)
for a in estudiante.values():
    print(a)
nombre=["juan","pablo","peres"]
ciudad=["guayaquil","ambato","guaranda"]
edad=[40,20,32]
for nombre, edad,ciudad in zip(nombre,edad,ciudad):
    print(nombre,edad,ciudad)
matriz = []
for i in range(3):
    fila = []
    for j in range(3):
        fila.append(i * 3 + j + 1)
    matriz.append(fila)

print("Matriz creada:")
for fila in matriz:
    print(fila)