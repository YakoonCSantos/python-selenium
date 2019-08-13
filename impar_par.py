from selenium import webdriver
from selenium.webdriver.common.keys import Keys


#informe o numero
n = int(input("informe um número! "))


#inicia o navegador, no caso o Google Chrome
navegador = webdriver.Chrome()

#navega para o google
navegador.get('file:///C:/Users/python/Desktop/python-selenium-master/IntroducaoWeb/impar_par.html')

#SELECIONA O PRIMEIRO INPUT
navegador.find_elements_by_tag_name('input')[0].send_keys(n)

#SELECIONA O PRIMEIRO INPUT
navegador.find_elements_by_tag_name('input')[1].click()

print("Resposta: É" + navegador.switch_to.alert.text)

navegador.switch_to.alert.accept()
input("Pressione Enter para fechar")

#fecha o navegador
navegador.close()