import requests
from bs4 import BeautifulSoup
import pandas as pd

texto_string = requests.get('https://revistaoeste.com/imprensa/revista-oeste-e-alvo-de-fake-news-de-aos-fatos/').text

bsp_texto = BeautifulSoup(texto_string, 'html.parser')
comentarios = bsp_texto.find_all('article', class_='comment-body')

lista_comentarios = []
# Itera sobre as tags dos comentários e extrai o texto de cada um
for comentario in comentarios:
    nome_usuario = comentario.find('b', class_='font-primary').text.strip()
    url_perfil = comentario.find('img', class_='avatar')['data-src']
    data_comentario = comentario.find('time').text.strip()
    comentario_feito = comentario.find('p').text.strip()

    lista_comentarios.append((nome_usuario, url_perfil, data_comentario, comentario_feito))

df_comentarios = pd.DataFrame(lista_comentarios, columns=['nome_usuario', 'url_foto_perfil', 'data_comentario', 'comentario_feito'])

print("\n")
print("Dados do usuário de ID 3")
conteudo_id_3 = df_comentarios.loc[2].to_frame().T
print(conteudo_id_3)

print("\n")
print("Comentário do usuário de ID 3")
conteudo_comentario_id_3 = df_comentarios.loc[2, 'url_foto_perfil']
print(conteudo_comentario_id_3)

print("\n")
print("Dataframe inteiro")
print(df_comentarios)

