import requests
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import json

url = 'https://stats.nba.com/players/traditional/?PerMode=Totals&Season=2019-20&SeasonType=Regular%20Season&sort=PLAYER_NAME&dir=-1'

options = Options()
driver = webdriver.Chrome() 
driver.get(url)
driver.implicitly_wait(5)  

# Abrindo o site no navegador

top10 = {}

rankings = {
    'points': {'field': 'PTS', 'label': 'PTS'},
    'assistants': {'field': 'AST', 'label': 'AST'},
    'rebounds': {'field': 'REB', 'label': 'REB'},
    'steals': {'field': 'STL', 'label': 'STL'},
    'blocks': {'field': 'BLK', 'label': 'BLK'},
    'vitorias': {'field': 'W','label':'W'}
}

# Definindo os campos do ranking 

def buildrank(type):

    field = rankings[type]['field']
    label = rankings[type]['label']

    driver.find_element_by_xpath(f"/html/body/div[3]/div[3]/div/div/div[2]/div/div/button").click()
    time.sleep(3)
    # Aceitando os cookies

    driver.find_element_by_xpath(f"/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[2]/div[1]/table/thead/tr/th[@data-field='{field}']").click() #Resolver isso
    # Clicando na tabela de pontos para ver o ranking 

    element = driver.find_element_by_xpath(f'/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[2]/div[1]/table')
    # Procurando a tabela no html 

    html_content = element.get_attribute('outerHTML')
    # Pegando o conteudo

    soup = BeautifulSoup(html_content, 'html.parser')
    # Parseando o htmli da página
    table = soup.find(name='table')
    # Encontrando a tabela

    df_full = pd.read_html(str (table))[0].head(10)

    df = df_full[['Unnamed: 0', 'PLAYER','TEAM',label]]
    df.columns = ['Posicao', 'Jogador', 'Time', 'Pontos']
    
    # Definindo o data frame

    return df.to_dict('records')
    # Retornando com um dicionario

for r in rankings:
    top10[r] = buildrank(r)

driver.quit()

with open('ranking.json', 'w', encoding='utf-8') as jp:
    js = json.dumps(top10, indent=4)
    jp.write(js)