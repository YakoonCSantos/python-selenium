from selenium import webdriver
from selenium.webdriver.common.keys import Keys

pesquisa = input("informe o que você deseja pesquisar! ")

#inicia o navegador, no caso o Google Chrome
navegador = webdriver.Chrome()

#navega para o google
navegador.get('https://www.google.com.br')

#preenche o campo de busca
#navegador.find_element_by_name('q').send_keys(pesquisa)
navegador.find_elements_by_tag_name('input')[2].send_keys(pesquisa)

#simula o usuário apertando a tecla enter, para ativar a busca
#navegador.find_element_by_name('q').send_keys(Keys.ENTER)
navegador.find_elements_by_tag_name('input')[2].send_keys(Keys.ENTER)

#Aguarda o usuário pressionar Enter
input('Pressione enter para finalizar')

#fecha o navegador
navegador.close()
