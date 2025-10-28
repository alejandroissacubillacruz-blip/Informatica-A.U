import os
hololive=["Watame","miko","korone","gura","sora","Aqua"]
for x in hololive:
    try:
        os.mkdir(x)
    except FileExistsError:
        print(f'la carpeta "{x}" ya existe')