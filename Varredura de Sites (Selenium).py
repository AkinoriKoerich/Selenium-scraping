from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os


# Abrir o navegador
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# acessar o site
driver.get('https://sitepreco1.netlify.app/')
# encontrar o abacate no site
precos_site_1 = driver.find_elements(By.XPATH,'//h6[@class="price_heading"]')
# anotar o valor
precos_final_site1 = precos_site_1[3].text.split(' ')[1]
print('parar')
# colocar na planilha

driver.get('https://sitepreco2.netlify.app/')
precos_site_2 = driver.find_elements(By.XPATH, "//h5")
preco_final_site2 = precos_site_2[3].text.split('$')[1]
print('teste')

driver.get('https://sitepreco3.netlify.app/')
precos_site_3 = driver.find_elements(By.XPATH, '//div[@class="featured__item__text"]//h5')
preco_final_site3 = precos_site_3[2].text.split('$')[1]

with open('precos.csv', 'w', newline='', encoding='utf-8') as arquivo:
    arquivo.write(f'Site, Preço{os.linesep}')
    arquivo.write(f'https://sitepreco1.netlify.app/, {precos_final_site1}{os.linesep}')
    arquivo.write(f'https://sitepreco2.netlify.app/, {preco_final_site2}{os.linesep}')
    arquivo.write(f'https://sitepreco3.netlify.app/, {preco_final_site3}{os.linesep}')
