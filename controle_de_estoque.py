from selenium import webdriver
from selenium.webdriver.common.keys import Keys


#informe o código do produto
produto1 = int(input("informe a quantidade de itens do produto 1! "))
produto2 = int(input("informe a quantidade de itens do produto 2! "))
produto3 = int(input("informe a quantidade de itens do produto 3! "))
produto4 = int(input("informe a quantidade de itens do produto 4! "))


#inicia o navegador, no caso o Google Chrome
navegador = webdriver.Chrome()


#navega para o google
navegador.get('file:///C:/Users/python/Desktop/python-selenium-master/IntroducaoWeb/html_css_javascript.html')

#click no adicionar produto
for item in range(0,produto1):
    #navegador.find_element_by_id('btn_1_add').click()
    navegador.find_elements_by_tag_name('button')[0].click()

for item in range(0,produto2):
    #navegador.find_element_by_id('btn_2_add').click()
    navegador.find_elements_by_tag_name('button')[2].click()

for item in range(0,produto3):
    #navegador.find_element_by_id('btn_3_add').click()
    navegador.find_elements_by_tag_name('button')[4].click()

for item in range(0,produto4):
    #navegador.find_element_by_id('btn_4_add').click()
    navegador.find_elements_by_tag_name('button')[6].click()

print("itens adcionados")

#fecha o navegador
navegador.close()

