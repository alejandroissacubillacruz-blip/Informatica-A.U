import time
from selenium import webdriver # Importar la librería selenium [6]
from selenium.webdriver.common.keys import Keys # Necesario para simular la tecla Enter [7]

def buscar_en_google_con_seleniuma(a):
    # 1. Ejecutar el driver de selenium (simula un navegador)
    driver = webdriver.Chrome() # Esto simula la apertura del navegador [6]
    
    # 2. Conectarse a Google
    driver.get("https://www.google.com") # Nos conectamos a Google [6]
    time.sleep(3) # Esperamos 3 segundos entre acciones [7]

    # 3. Buscar el elemento de la caja de búsqueda
    # El elemento de la caja de búsqueda en Google tiene el atributo 'name' igual a 'q' [6]
    try:
        caja_busqueda = driver.find_element("name", "q") # [6]
    except Exception as e:
        print(f"Error al encontrar la caja de búsqueda: {e}")
        driver.quit()
        return

    # 4. Escribir en el buscador
    caja_busqueda.send_keys(a) # Escribimos el texto en la caja de búsqueda [7]
    time.sleep(3) # Esperamos 3 segundos [7]

    # 5. Realizar la búsqueda
    caja_busqueda.send_keys(Keys.RETURN) # Enviamos la tecla Enter para ejecutar la búsqueda [7]
    
    # Opcional: El navegador permanecerá abierto mostrando los resultados de la búsqueda [8].

# Ejecutar la función
print("bienvenidos al buscador automatizado")
busqueda=(input("ingrese el termino que desea buscar: "))
buscar_en_google_con_seleniuma(busqueda)