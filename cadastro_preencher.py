"""
from selenium import webdriver

chrome = webdriver.Chrome()

chrome.get('file:///C:/src/python-selenium/cadastro.html')

chrome.find_element_by_id('firstName').send_keys('Rodrigo')
chrome.find_element_by_id('lastName').send_keys('Campos')
chrome.find_element_by_id('address').send_keys('Av. Abc')
chrome.find_element_by_id('address2').send_keys('Apto 123')

[p for p in chrome.find_elements_by_xpath("//select[@id='country']/option") if p.text == "Brasil"][0].click()
[e for e in chrome.find_elements_by_xpath("//select[@id='state']/option") if e.text == "São Paulo"][0].click()

chrome.find_element_by_id('zip').send_keys('00000-000')

act = webdriver.ActionChains(chrome)
act.move_to_element(chrome.find_element_by_id('gender_f')).click().perform()

act = webdriver.ActionChains(chrome)
act.move_to_element(chrome.find_element_by_id('steal-data'))
act.click().perform()

chrome.find_element_by_id('document').send_keys(r'C:\src\python-selenium\cadastro_simples.py')

chrome.find_element_by_xpath('//button').click()
alert = chrome.switch_to.alert

print('resultado: {}'.format(alert.text))
alert.accept()

chrome.switch_to.default_content
chrome.back()

input('Pressione enter para finalizar')
chrome.close()  




from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


#inicia o navegador, no caso o Google Chrome
navegador = webdriver.Chrome()

#navega para o google
navegador.get('file:///C:/Users/python/Desktop/python-selenium-master/cadastro.html')
#
navegador.find_element_by_id('firstName').send_keys('Tiago')
#
navegador.find_element_by_id('lastName').send_keys('Santos')
#
navegador.find_element_by_id('email').send_keys('tiagosantos@teste.com.br')
#
navegador.find_element_by_id('address').send_keys('Rua dos bobos')
#
navegador.find_element_by_id('address2').send_keys('nº 0')
#
[pais for pais in navegador.find_elements_by_xpath("//select[@id='country']/option") if pais.text =="Brasil"] [0].click()
#
[estado for estado in navegador.find_elements_by_xpath("//select[@id='state']/option") if estado.text =="São Paulo"] [0].click()
#
navegador.find_element_by_id('zip').send_keys('00000-000')

acao = webdriver.ActionChains(navegador)

acao.move_to_element(navegador.find_element_by_id('gender_m')).click().perform()
#acao.move_to_element(navegador.find_element_by_id('accept-terms')).click().perform()
acao.move_to_element(navegador.find_element_by_id('steal-data')).click().perform()

#
filename = "teste.png"
navegador.save_screenshot(filename)

#
navegador.find_element_by_id('document').send_keys(r'C:\Users\python\Desktop\teste.png')

#Time para visualizar a interação
time.sleep(2.0)

navegador.find_element_by_xpath('//button').click()

#Time para visualizar a interação
time.sleep(2.0)

#
alert = navegador.switch_to.alert
print('resultado: {}'.format(alert.text))
alert.accept()
navegador.switch_to.default_content




#Anterior
navegador.back()


#atualizar
navegador.refresh()


#Time para visualizar a interação
time.sleep(10.0)


#fecha o navegador
navegador.close()


#lib para validar cep
import pycep_correios

#>>> endereco = pycep_correios.consultar_cep('37503130')
#>>> print(endereco)
{
    'bairro': 'Santo Antônio',
    'cep': '37503130',
    'cidade': 'Itajubá',
    'end': 'Rua Geraldino Campista',
    'uf': 'MG',
    'complemento2': '- até 214/215',
}


"""

f = open('‪C:\Users\python\Desktop\cadastro.csv', 'r')
for linha in f:
  print(linha)
f.close()



