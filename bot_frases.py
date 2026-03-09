from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv
navegador =webdriver.Firefox()
navegador.get("http://quotes.toscrape.com/")
time.sleep(2)

with open ('datos_recuperados.csv', mode = 'w',encoding ='utf-8') as document:
    escritor = csv.writer(document)
    lista_tarjetas = navegador.find_elements(By.CLASS_NAME,"quote")
    for tarjeta in lista_tarjetas:
        frase = tarjeta.find_element(By.CLASS_NAME,"text")
        autor = tarjeta.find_element(By.CLASS_NAME,"author")

        escritor.writerow([frase.text, autor.text])

navegador.quit()