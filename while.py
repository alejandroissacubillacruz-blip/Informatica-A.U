numeros=[]
suma=0
num=int(input("ingrese un numero: "))
while True:
    numeros.append(num)
    num=int(input("ingrese otro numero: "))
    if num ==0:
        break
for x in numeros:
    suma+=x
print(f"la suma de {numeros} es igual a {suma}")
