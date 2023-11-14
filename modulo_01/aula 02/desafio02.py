import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime


url = 'https://ge.globo.com/'

texto_string = requests.get(url).text
bsp_texto = BeautifulSoup(texto_string, 'html.parser')
artigos_disponiveis = bsp_texto.find_all('div', class_='feed-post-body')

lista_artigos = []
for artigo in artigos_disponiveis:

    manchete = artigo.find('div', class_='_evt').text.strip()

    # Verifica se há descrição, senão atribui "Sem descrição"
    descricao_element = artigo.find('div', class_='feed-post-body-resumo')
    descricao = descricao_element.text.strip() if descricao_element else 'Sem descrição'

    link = artigo.find('a')['href']

    # Verifica se há descrição, senão atribui "Sem descrição"
    secao_element = artigo.find('span', class_='feed-post-header-chapeu')
    secao = secao_element.text.strip() if secao_element else 'Sem Secao Definida'
    
    hora_extracao = datetime.datetime.now()

    # Noticia postada a quanto tempo
    time_delta_element = artigo.find('span', class_='feed-post-datetime')
    time_delta = time_delta_element.text.strip() if time_delta_element else 'Sem hora definida'
    
    lista_artigos.append((manchete, descricao, link, secao, hora_extracao, time_delta))

df_artigosGE = pd.DataFrame(lista_artigos, columns=['manchete', 'descricao', 'link', 'secao', 'hora_extracao', 'time_delta'])
print("\n")
print("Dataframe inteiro")
print(df_artigosGE)
print("\n")