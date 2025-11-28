import os
for x in range(1,16):
    try:
        os.mkdir(f"carpeta_{x}")
    except FileExistsError:
        print(f'la carpeta "{x}" ya existe')