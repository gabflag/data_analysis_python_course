import pandas as pd


def introducao_criacao_series():
    # Para construir um objeto do tipo Series, precisamos utilizar o método Series() 
    # O método possui o seguinte construtor: pandas.Series(data=None, index=None, dtype=None, name=None, copy=False, fastpath=False).
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html
   
    print("\n############")
    print(" # Cria uma Series com o unico dado obrigatório")
    serie = pd.Series(data='Primeiro da Série')
    print(serie)

    print("\n############")
    print(" # Cria uma Series com uma Lista")
    lista_nomes = 'Howard Ian Peter Jonah Kellie'.split()
    nomes = pd.Series(lista_nomes)
    print(nomes)

    print("\n############")
    print(" # Cria uma Series com um dicionário")
    dados = {
        'nome1': 'Howard',
        'nome2': 'Ian',
        'nome3': 'Peter',
        'nome4': 'Jonah',
        'nome5': 'Kellie',
    }
    dicionario = pd.Series(dados)
    print(dicionario)

    print("\n############")
    print(" # Cria uma Series com uma Lista e utiliza uma outra lista para os rotulos")
    cpfs = '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44 555.555.555-55'.split()
    nome_e_cpf = pd.Series(lista_nomes, index=cpfs)
    print(nome_e_cpf)


    print("\n############")
    print(" # Localizando por identificador '111.111.111-11': ")
    print(nome_e_cpf.loc['111.111.111-11'])


def extraindo_dados_serie():
    series_dados = pd.Series([10.2, -1, None, 15, 23.4])

    print('Quantidade de linhas = ', series_dados.shape) # Retorna uma tupla com o número de linhas
    print('Tipo de dados', series_dados.dtypes) # Retorna o tipo de dados, se for misto será object
    print('Os valores são únicos?', series_dados.is_unique) # Verifica se os valores são únicos (sem duplicações)
    print('Existem valores nulos?', series_dados.hasnans) # Verifica se existem valores nulos
    print('Quantos valores existem?', series_dados.count()) # Conta quantas valores existem (excluí os nulos)

    print('Qual o menor valor?', series_dados.min()) # Extrai o menor valor da Series (nesse caso os dados precisam ser do mesmo tipo)
    print('Qual o maior valor?', series_dados.max()) # Extrai o valor máximo, com a mesma condição do mínimo
    print('Qual a média aritmética?', series_dados.mean()) # Extrai a média aritmética de uma Series numérica
    print('Qual o desvio padrão?', series_dados.std()) # Extrai o desvio padrão de uma Series numérica
    print('Qual a mediana?', series_dados.median()) # Extrai a mediana de uma Series numérica

    print('\nResumo:\n', series_dados.describe()) # Exibe um resumo sobre os dados na Series


def introducao_dataframe():
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html
    # Dentre todos os parâmetros esperados, somente um é obrigatório para se criar um DataFrame com dados, o parâmetro data=XXXX.
    # assim como na serie
    # Esse parâmetro pode receber, um objeto iterável, como uma lista, tupla, um dicionário ou um DataFrame, vejamos os exemplos.
    lista_nomes = 'Howard Ian Peter Jonah Kellie'.split()
    lista_cpfs = '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44 555.555.555-55'.split()
    lista_emails = 'risus.varius@dictumPhasellusin.ca Nunc@vulputate.ca fames.ac.turpis@cursusa.org non@felisullamcorper.org eget.dictum.placerat@necluctus.co.uk'.split()
    lista_idades = [32, 22, 25, 29, 38]
    
    myframe = pd.DataFrame(lista_nomes, columns=['nome'])
    myframe = pd.DataFrame(lista_nomes, columns=['nome'], index=lista_cpfs)

    dados = list(zip(lista_nomes, lista_cpfs, lista_idades, lista_emails)) # cria uma lista de tuplas
    myframe = pd.DataFrame(dados, columns=['nome', 'cpfs', 'idade', 'email'])
    # print(myframe)

    dados = {
        'nomes': 'Howard Ian Peter Jonah Kellie'.split(),
        'cpfs' : '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44 555.555.555-55'.split(),
        'emails' : 'risus.varius@dictumPhasellusin.ca Nunc@vulputate.ca fames.ac.turpis@cursusa.org non@felisullamcorper.org eget.dictum.placerat@necluctus.co.uk'.split(),
        'idades' : [32, 22, 25, 29, 38]
    }
    myframeDictionary = pd.DataFrame(dados)
    print(myframeDictionary)


def extraindo_dados_dataframe():
    dados = {
        'nomes': 'Howard Ian Peter Jonah Kellie'.split(),
        'cpfs' : '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44 555.555.555-55'.split(),
        'emails' : 'risus.varius@dictumPhasellusin.ca Nunc@vulputate.ca fames.ac.turpis@cursusa.org non@felisullamcorper.org eget.dictum.placerat@necluctus.co.uk'.split(),
        'idades' : [32, 22, 25, 29, 38]
    }
    df_dados = pd.DataFrame(dados)
    print(df_dados)
    
    print('\nInformações do DataFrame:\n')
    print(df_dados.info()) # Apresenta informações sobre a estrutura do DF

    print('\nQuantidade de linhas e colunas = ', df_dados.shape) # Retorna uma tupla com o número de linhas e colunas
    print('\nTipo de dados:\n', df_dados.dtypes) # Retorna o tipo de dados, para cada coluna, se for misto será object

    print('\nQual o menor valor de cada coluna?\n', df_dados.min()) # Extrai o menor de cada coluna
    print('\nQual o maior valor?\n', df_dados.max()) # Extrai o valor máximo e cada coluna 
    print('\nQual a média aritmética?\n', df_dados.select_dtypes(include=['number']).mean()) # Extrai a média aritmética de cada coluna numérica
    print('\nQual o desvio padrão?\n', df_dados.select_dtypes(include=['number']).std()) # Extrai o desvio padrão de cada coluna numérica
    print('\nQual a mediana?\n', df_dados.select_dtypes(include=['number']).median()) # Extrai a mediana de cada coluna numérica

    print('\nResumo:\n', df_dados.describe()) # Exibe um resumo

    df_dados.head() # Exibe os 5 primeiros registros do DataFrame


def operacoes_df_por_colunas():
    # Para selecionar uma coluna, as duas possíveis sintaxes são:
        # nome_df.nome_coluna
        # nome_df[nome_coluna]

    # precisarmos selecionar mais do que uma coluna, então precisamos passar uma lista, da seguinte forma: nome_df[['col1', 'col2', 'col3']]
    dados = {
        'nomes': 'Howard Ian Peter Jonah Kellie'.split(),
        'cpfs' : '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44 555.555.555-55'.split(),
        'emails' : 'risus.varius@dictumPhasellusin.ca Nunc@vulputate.ca fames.ac.turpis@cursusa.org non@felisullamcorper.org eget.dictum.placerat@necluctus.co.uk'.split(),
        'idades' : [32, 22, 25, 29, 38]
    }
    df_dados = pd.DataFrame(dados)
    df_uma_coluna = df_dados['idades']
    print(type(df_uma_coluna))

    print('Média de idades = ', df_uma_coluna.mean())
    print("######\n")

    colunas = ['nomes', 'cpfs']
    df_duas_colunas = df_dados[colunas]
    print(type(df_duas_colunas))
    print(df_duas_colunas)


def dados_estruturados():
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_html.html  
    # A biblioteca possui uma série de métodos "read", cuja sintaxe é: pandas.read_XXXXX() onde a sequência de X representa as diversas opções disponíveis
    
    url = 'https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/'
    df_estruturado = pd.read_html(url)

    print(type(df_estruturado))
    print(len(df_estruturado))

    
    df_bancos = df_estruturado[0]

    print(df_bancos.shape)
    print(df_bancos.dtypes)

    df_bancos.head()

    print(df_bancos)

extraindo_dados_dataframe()
