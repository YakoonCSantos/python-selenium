from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


#inicia o navegador, no caso o Google Chrome
navegador = webdriver.Chrome()

#navega para o google
navegador.get('https://www.instagram.com/explore/locations/c269969/sao-paulo-brazil/')


#Time para visualizar a interação
time.sleep(2.0)


#[pais for pais in navegador.find_elements_by_xpath("//select[@id='country']/option") if pais.text =="Brasil"] [0].click()
