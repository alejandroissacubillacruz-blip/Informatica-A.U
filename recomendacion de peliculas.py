def recomendar_película(a,b):
    if a=="accion":
        if b >=13:
            print("te recomiendo que veas Deadpool")
        else:
            print("te recomiendo que veas Regreso al futuro")
    elif a=="comedia":
        print(" te recomiendo que veas Aterriza como puedas")
    else:
        print("te recomiendo que explores otros generos")

genero=input("¿cual es tu genero favorito?: ")
edad=int(input("¿Cual es tu edad?: "))
recomendar_película(genero,edad)