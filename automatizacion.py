import time
from selenium import webdriver # Importar la librería selenium [6]
from selenium.webdriver.common.keys import Keys # Necesario para simular la tecla Enter [7]

def buscar_en_google_con_selenium():
    # 1. Ejecutar el driver de selenium (simula un navegador)
    driver = webdriver.Chrome() # Esto simula la apertura del navegador [6]
    
    # 2. Conectarse a Google
    driver.get("https://classroom.google.com/a/not-turned-in/all") # Nos conectamos a Google [6]
    time.sleep(3)
buscar_en_google_con_selenium()