#ingreso de numero
num=int(input("ingrese un numero que vas a convertir a binario: "))
#el numero ingresado se guarda en otra variable para evitar cambio
num2=num
#se crea un uno "binario" y otra "residuos" como auxiliar o adicional
residuos=[]
binario=""
#despues de meter num a num2, con num se calcula repetitivamente hasta que num quede en 0
#ahi se añade los residuos de cada division a la lista
while num >= 1:
#antes de dividir se calcula el residuo o modulo de la mitad
    residuos.append(num%2)
#luego se divide por esa mitad para luego añadir otro residuo mas el la lista
    num//=2
#luego de añadirlos residuos a la lista, se cuenta la cantidad de residuo a la otra variable y se resta 1
cantidad_de_residuos=len(residuos)-1
# donde e ciclo se finaliza despues de que la variable de cantidad llegue al numero negativo
#ahi se añade cada dato de la lista en reversa
while cantidad_de_residuos>=0:
#se añade a "binario" en forma de string, una dato asignado por "cantidad" de lista de residuos
    binario+=str(residuos[cantidad_de_residuos])
#luego se resta la variable
    cantidad_de_residuos-=1
#por ultimo se imprime num2 y "binario"
print(f"{num2} en binario es {binario}")