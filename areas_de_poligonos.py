def calculo_area(a,b,triangulo):
    #multiplico lado por lado o base por altura
    area=a*b
#se divide por la mitad solo si es un triangulo
    if triangulo:
        area/=2
#luego la funcion me devuelve el resultado
    return area
print("''areas de las tres formas regulares''")
print("triangulo")
lado_triangulo=int(input("ingrese la medida de cada uno de sus lados: "))
#me enfoco por la mitad del triangulo y aplico el teorema de pitagoras
#h^2= base^2+altura^2  ;   altura= raiz_cuadrada(h^2-base^2)
altura=((lado_triangulo**2)-((lado_triangulo/2)**2))**(1/2)
#envio la base y la altura a la funcion y guardo en una variable
#el true lo uso para decir que es un triangulo
area_triangulo=calculo_area(lado_triangulo,altura,True)
print("")
print("cuadrado")
lado_cuadrado=int(input("ingrese la medida de cada uno de sus lados: "))
#su area es lado^2 que es como decir lado por lado, y un false para decirle a la funcion que no es un triangulo
area_cuadrado=calculo_area(lado_cuadrado,lado_cuadrado,False)
print("")
print("rectangulo")
lado_rectangulo_H=int(input("ingrese el lado horinzontal del rectangulo: "))
lado_triangulo_V=int(input("ingrese el lado vertical del rectangulo: "))
#los lados hrizontales y verticales lo envio a la funcion y lo mismo indentifico que no es un triangulo
area_rectangulo=calculo_area(lado_rectangulo_H,lado_triangulo_V,False)
#finalmente demuestro las areas de cada uno
print(f"\nel area del triangulo es {area_triangulo}, el del cuadradro es {area_cuadrado} y el del rectangulo es {area_rectangulo}")