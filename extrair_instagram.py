from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#inicia o navegador, no caso o Google Chrome
navegador = webdriver.Chrome()

#navega para o google
navegador.get('https://www.instagram.com/viajante_roots/')

encontrar_links = navegador.find_elements_by_tag_name('a')

links = [l.get_attribute('href') for l in encontrar_links]

for item in links:
    print(item)

#fecha o navegador
navegador.close()