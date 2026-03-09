from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
navegador =webdriver.Firefox()
navegador.get("http://quotes.toscrape.com/")
time.sleep(2)
lista_tarjetas = navegador.find_elements(By.CLASS_NAME,"quote")
for tarjeta in lista_tarjetas:
    frases= tarjeta.find_element(By.CLASS_NAME,"text")
    autor= tarjeta.find_element(By.CLASS_NAME,"author")
    print(f"{frases.text}--- Author {autor.text}")
    print("")

navegador.quit()