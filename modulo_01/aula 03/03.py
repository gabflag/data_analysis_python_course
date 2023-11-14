# Todos os métodos capazes de fazer a leitura dos dados estruturados possuem prefixo pd.read_XXX, 
#  Além de fazer a leitura a biblioteca possui diversos métodos capazes de escrever o DataFrame em
# um arquivo, em um banco ou ainda simplesmente copiar para a área de transferência do sistema operacional. 
# CSV (comma-separated values - valores separados por vírgula)  

import pandas as pd
from datetime import date
from datetime import datetime as dt

def criar_df():
    # GET DATAS
    df_selic = pd.read_json("https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json")

    # REMOVER LINHAS DUPLICADAS
    df_selic.drop_duplicates(keep='last', inplace=True)

    # CRIAR NOVAS COLUNAS
    data_extracao = date.today()
    df_selic['Data_Extracao'] = data_extracao
    df_selic['Tecnico_extracao'] = 'GabFlag'

    #  ALTERAR O TIPO DOS DADOS
    df_selic['data'] = pd.to_datetime(df_selic['data'], dayfirst=True)
    df_selic['Data_Extracao'] = df_selic['Data_Extracao'].astype('datetime64[ns]')

    # PADRONIZANDO STRINGS
    df_selic['Tecnico_extracao'] = df_selic['Tecnico_extracao'].str.upper()
    
    # ORDENANDO UM DATAFRAME COM BASE EM UMA COLUNA (OS INDEXES PERMANECEM OS MESMOS)
    df_selic.sort_values(by='data', ascending=False, inplace=True)

    # RESETANDO OS INDEX
    df_selic.reset_index(drop=True, inplace=True)
    
    # OU PODEMOS SETAR O VALOR QUE TERÁ NO INDEX
    lista_novos_index = [f'selic_{indice}' for indice in df_selic.index]
    df_selic.set_index(keys=[lista_novos_index], inplace=True)
    
    return df_selic


def read_json_file():
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_json.html

    json = pd.read_json("https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json").head()
    print(json)


def read_csv_file():
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html.
    # Outro parâmetro que é importante para a leitura desse arquivo é o sep ou delimiter (ambos fazem a mesma coisa),
    # veja que sep, por padrão possui o valor ',', ou seja, caso não seja especificado nenhum valor, então o método 
    # fará a leitura dos dados considerando que estão separados por vírgula. O parâmetro header, tem como valor padrão
    # 'infer', que significa que o método realiza a inferência para os nomes das colunas a partir da primeira linha
    # de dados do arquivo.
    csv = pd.read_csv("https://people.sc.fsu.edu/~jburkardt/data/csv/cities.csv").head()
    print(csv)


def manipulacao_taxa_selic_01():
    # GET DATAS
    df_selic = pd.read_json("https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json")
    print(df_selic.info())

    # REMOVER LINHAS DUPLICADAS
    # usamos o método  para remover as linhas duplicadas, pedindo para manter o último registro (keep='last')
    # Caso inplace não seja passado, a transformação é aplicada, mas não é salva, ou seja, o DF continua da 
    # mesma forma anterior a transformação.
    df_selic.drop_duplicates(keep='last', inplace=True)

    # CRIAR NOVAS COLUNAS
    data_extracao = date.today()
    df_selic['Data_Extracao'] = data_extracao
    df_selic['Tecnico_extracao'] = 'GabFlag'

    print(df_selic.info())
    print(df_selic.head())


def manipulacao_taxa_selic_02():
    # MÉTODO TO_DATETIME() E ASTYPE()
    # ano-mês-dia é um padrão do datetime64[ns],
    # Poderíamos usar o stftime() para transformar o traço em barra (/), mas aí o resultado seriam strings e não datas.
    # Organizando DF (inplace=True) significa que queremos modificar o próprio objeto, na prática estamos sobrescrevendo o DF.

    # GET DATAS
    df_selic = pd.read_json("https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json")
    print(df_selic.info())

    # REMOVER LINHAS DUPLICADAS
    df_selic.drop_duplicates(keep='last', inplace=True)

    # CRIAR NOVAS COLUNAS
    data_extracao = date.today()
    df_selic['Data_Extracao'] = data_extracao
    df_selic['Tecnico_extracao'] = 'GabFlag'

    #  ALTERAR O TIPO DOS DADOS
    df_selic['data'] = pd.to_datetime(df_selic['data'], dayfirst=True)
    df_selic['Data_Extracao'] = df_selic['Data_Extracao'].astype('datetime64[ns]')

    # PADRONIZANDO STRINGS
    df_selic['Tecnico_extracao'] = df_selic['Tecnico_extracao'].str.upper()
    
    
    # ORDENANDO UM DATAFRAME COM BASE EM UMA COLUNA (OS INDEXES PERMANECEM OS MESMOS)
    df_selic.sort_values(by='data', ascending=False, inplace=True)

    # RESETANDO OS INDEX
    df_selic.reset_index(drop=True, inplace=True)
    
    # OU PODEMOS SETAR O VALOR QUE TERÁ NO INDEX
    lista_novos_index = [f'selic_{indice}' for indice in df_selic.index]
    df_selic.set_index(keys=[lista_novos_index], inplace=True)

    print(df_selic.info())
    print(df_selic.head())

    print("############")
    # Menor valor de uma coluna do DF
    print(df_selic['valor'].idxmin())

    # Maior valor de uma coluna do DF
    print(df_selic['valor'].idxmax())


def filtros_com_loc():
    # GET DATAS
    df_selic = pd.read_json("https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json")

    # REMOVER LINHAS DUPLICADAS
    df_selic.drop_duplicates(keep='last', inplace=True)

    # CRIAR NOVAS COLUNAS
    data_extracao = date.today()
    df_selic['Data_Extracao'] = data_extracao
    df_selic['Tecnico_extracao'] = 'GabFlag'

    #  ALTERAR O TIPO DOS DADOS
    df_selic['data'] = pd.to_datetime(df_selic['data'], dayfirst=True)
    df_selic['Data_Extracao'] = df_selic['Data_Extracao'].astype('datetime64[ns]')

    # PADRONIZANDO STRINGS
    df_selic['Tecnico_extracao'] = df_selic['Tecnico_extracao'].str.upper()
    
    # ORDENANDO UM DATAFRAME COM BASE EM UMA COLUNA (OS INDEXES PERMANECEM OS MESMOS)
    df_selic.sort_values(by='data', ascending=False, inplace=True)

    # RESETANDO OS INDEX
    df_selic.reset_index(drop=True, inplace=True)
    
    # OU PODEMOS SETAR O VALOR QUE TERÁ NO INDEX
    lista_novos_index = [f'selic_{indice}' for indice in df_selic.index]
    df_selic.set_index(keys=[lista_novos_index], inplace=True)


    print(df_selic.loc['selic_0'])
    print("")

    print(df_selic.loc[['selic_0', 'selic_4', 'selic_200']])
    print("")

    print(df_selic.loc[:'selic_11'])
    print("")
    
    # A propriedade loc, aceita um segundo argumento, que é a coluna (ou colunas) que serão exibidas para os índices escolhidos. 
    # df_selic.loc[['selic_0', 'selic_4', 'selic_200'], 'valor']
    # df_selic.loc[['selic_0', 'selic_4', 'selic_200'], ['valor', 'data_extracao']]
    print(df_selic.loc[:'selic_11']['valor'])
    print("")

    print(df_selic.loc[['selic_0', 'selic_4', 'selic_200'], ['valor', 'Data_Extracao']])
    print('')

    # PODE SER FILTRADO COM O ILOC, MAS ESSA NÃO CONSEGUIMOS PASSAR CONDIÇÕES BOOLEANAS
    print(df_selic.iloc[:11])

  
def filtros_booleanos():
    # GET DATAS
    df_selic = pd.read_json("https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json")

    # REMOVER LINHAS DUPLICADAS
    df_selic.drop_duplicates(keep='last', inplace=True)

    # CRIAR NOVAS COLUNAS
    data_extracao = date.today()
    df_selic['Data_Extracao'] = data_extracao
    df_selic['Tecnico_extracao'] = 'GabFlag'

    #  ALTERAR O TIPO DOS DADOS
    df_selic['data'] = pd.to_datetime(df_selic['data'], dayfirst=True)
    df_selic['Data_Extracao'] = df_selic['Data_Extracao'].astype('datetime64[ns]')

    # PADRONIZANDO STRINGS
    df_selic['Tecnico_extracao'] = df_selic['Tecnico_extracao'].str.upper()
    
    # ORDENANDO UM DATAFRAME COM BASE EM UMA COLUNA (OS INDEXES PERMANECEM OS MESMOS)
    df_selic.sort_values(by='data', ascending=False, inplace=True)

    # RESETANDO OS INDEX
    df_selic.reset_index(drop=True, inplace=True)
    
    # OU PODEMOS SETAR O VALOR QUE TERÁ NO INDEX
    lista_novos_index = [f'selic_{indice}' for indice in df_selic.index]
    df_selic.set_index(keys=[lista_novos_index], inplace=True)

    print("Valor da taxa é maior que 0.01: ")
    teste = df_selic['valor'] > 0.01
    print(teste[:5])
    print("")

    print("O ano da taxa é de 2023: ")
    teste02 = df_selic['data'] >= pd.to_datetime('2023-01-01')
    print(teste02[:5])


def condicionais():
    '''
    Para a operação lógica AND (E), em pandas, usa-se o caracter &. Para fazer 
    a operação lógica OR (OU), usa-se o caracter |. Cada teste deve estar 
    entre parênteses, senão ocorre um erro. 
    '''
    # GET DATAS
    df_selic = pd.read_json("https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json")

    # REMOVER LINHAS DUPLICADAS
    df_selic.drop_duplicates(keep='last', inplace=True)

    # CRIAR NOVAS COLUNAS
    data_extracao = date.today()
    df_selic['Data_Extracao'] = data_extracao
    df_selic['Tecnico_extracao'] = 'GabFlag'

    #  ALTERAR O TIPO DOS DADOS
    df_selic['data'] = pd.to_datetime(df_selic['data'], dayfirst=True)
    df_selic['Data_Extracao'] = df_selic['Data_Extracao'].astype('datetime64[ns]')

    # PADRONIZANDO STRINGS
    df_selic['Tecnico_extracao'] = df_selic['Tecnico_extracao'].str.upper()
    
    # ORDENANDO UM DATAFRAME COM BASE EM UMA COLUNA (OS INDEXES PERMANECEM OS MESMOS)
    df_selic.sort_values(by='data', ascending=False, inplace=True)

    # RESETANDO OS INDEX
    df_selic.reset_index(drop=True, inplace=True)
    
    # OU PODEMOS SETAR O VALOR QUE TERÁ NO INDEX
    lista_novos_index = [f'selic_{indice}' for indice in df_selic.index]
    df_selic.set_index(keys=[lista_novos_index], inplace=True)

    print("Resultado utilizando o AND: \n")
    teste03 = (df_selic['valor'] > 0.01 ) & (df_selic['data'] >= pd.to_datetime('2023-01-01'))
    print(teste03[:5])

    print("Resultado utilizando o OR: \n")
    teste04 = (df_selic['valor'] > 0.01 ) | (df_selic['data'] >= pd.to_datetime('2023-01-01'))
    print(teste04[:5])


def criando_filtros_e_salvando_em_arquivos():
    # GET DATAS
    df_selic = criar_df()
    filtro1 = df_selic['valor'] < 0.01
    print(df_selic.loc[filtro1])

    print('\nFiltro de Janeiro de 2015: \n')
    data1 = pd.to_datetime('2015-01-01')
    data2 = pd.to_datetime('2015-01-31')

    filtro_janeiro_2015 = (df_selic['data'] >= data1) & (df_selic['data'] <= data2)
    df_janeiro_2015 = df_selic.loc[filtro_janeiro_2015]
    print(df_janeiro_2015.head)

    print('\nFiltro de Janeiro de 2023: \n')
    data1 = pd.to_datetime('2023-01-01')
    data2 = pd.to_datetime('2023-01-31')

    filtro_janeiro_2023 = (df_selic['data'] >= data1) & (df_selic['data'] <= data2)
    df_janeiro_2023 = df_selic.loc[filtro_janeiro_2023]
    print(df_janeiro_2023.head)

    print("\n### Análise dos dados: ")
    print("Minimo Geral = ", df_selic['valor'].min())
    print("Minimo janeiro 2015 = ", df_janeiro_2015['valor'].min())
    print("Minimo janeiro 2023 = ", df_janeiro_2023['valor'].min())
    print('')
    print("Máximo Geral = ", df_selic['valor'].max())
    print("Máximo janeiro 2015 = ", df_janeiro_2015['valor'].max())
    print("Máximo janeiro 2023 = ", df_janeiro_2023['valor'].max())
    print('')
    print("Média Geral = ", df_selic['valor'].mean())
    print("Média janeiro 2015 = ", df_janeiro_2015['valor'].mean())
    print("Média janeiro 2023 = ", df_janeiro_2023['valor'].mean())

    df_janeiro_2015.to_csv('dados_selic_janeiro_2015.csv')


def criando_database():
    '''
    A biblioteca pandas possui dois métodos que permitem executar instruções SQL em banco de dados. Os métodos são:

    pandas.read_sql(sql, con, index_col=None, coerce_float=True, params=None, parse_dates=None, columns=None, chunksize=None)
    pandas.read_sql_query(sql, con, index_col=None, coerce_float=True, params=None, parse_dates=None, chunksize=None)
    
    A conexão com o banco de dados, deve ser feita usando uma outra biblioteca, por exemplo, sqlalchemy (suporte para diversos bancos),
    pyodbc para SQL Server, cx_Oracle para Oracle, psycopg2 para Postgresql, dentre outras. Seguindo as recomendações da PEP 249 todas
    bibliotecas precisam fornecer um método "connect", o qual recebe a string de conexão. A síntaxe da string de conexão
    depende da biblioteca e do banco de dados.
    
    import psycopg2


    # POSTGRESS

    host = 'XXXXX'
    port = 'XXXXX'
    database = 'XXXXX'
    username = 'XXXXX'
    password = 'XXXXX'

    conn_str = fr"dbname='{database}' user='{username}' host='{host}' password='{password}' port='{port}'"
    conn = psycopg2.connect(conn_str)

    query = "select * from XXX.YYYY"
    df = pd.read_sql(query, conn)import mysql.connector

    
    # MYSQL
    host = 'XXXXX'
    port = 'XXXXX'
    database = 'XXXXX'
    username = 'XXXXX'
    password = 'XXXXX'

    conn_str = fr"host={host}, user={username}, passwd={password}, database={database}"
    conn = mysql.connector.connect(host="localhost", user="root", passwd="", database="bd")

    query = "select * from XXX.YYYY"
    df = pd.read_sql(query, conn)
    '''
    pass


criando_filtros_e_salvando_em_arquivos()