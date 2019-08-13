from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#inicia o navegador, no caso o Google Chrome
navegador = webdriver.Chrome()

#navega para o google
navegador.get('https://play.google.com/store/apps/details?id=com.whatsapp.w4b')

def nome:
    try:
        return navegador.find_element_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz[3]/div/div[2]/div/div[1]/div/c-wiz[1]/c-wiz[1]/div/div[2]/div/div[1]/c-wiz[1]/h1').text
    except:
        return ""

def resumo:
    try:
        return navegador.find_element_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz[3]/div/div[2]/div/div[1]/div/c-wiz[1]/c-wiz[3]/div/div[1]/div[2]/div[1]/span/div').text
    except:
        return ""

def nota: 
    try:
        return navegador.find_element_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz[3]/div/div[2]/div/div[1]/div/div/div[1]/c-wiz/div[1]/div[1]').text
    except:
        return ""

def total_avaliacao:
    try:
        return navegador.find_element_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz[3]/div/div[2]/div/div[1]/div/div/div[1]/c-wiz/div[1]/span/span[2]').text
    except:
        return ""

def avaliacao_nome:
    try:
        return navegador.find_element_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz[3]/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div/div[2]/div[1]/div[1]/span').text
    except:
        return ""

def avaliacao_data:
    try:
        return navegador.find_element_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz[3]/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div/div[2]/div[1]/div[1]/div/span[2]').text
    except:
        return ""

def avaliacao_nota:
    try:
        return navegador.find_element_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz[3]/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div/div[2]/div[1]/div[1]/div/span[1]/div/div').text
    except:
        return ""

def avaliacao_resumo:
    try:
        return navegador.find_element_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz[3]/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div/div[2]/div[2]/span[2]').text
    except:
        return ""

print('')
    