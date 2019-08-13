from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#inicia o navegador, no caso o Google Chrome
navegador = webdriver.Chrome()

#navega para o google
navegador.get('file:///C:/Users/python/Desktop/python-selenium-master/IntroducaoWeb/javascript.html')

#navegador.find_element_by_name('btn_exibirhora').click()

#UTILIZANDO O RANGE A ORDEN INICIA A PARTIR DE 0,1,2... E NÃO 1,2,3
navegador.find_elements_by_tag_name('button')[1].click()

#resultado = navegador.find_element_by_id('minha_div').text
resultado = navegador.find_element_by_tag_name('span').text

print("Agora são exatamente:", resultado)

#fecha o navegador
navegador.close()
