import pandas as pd

'''
- Em cada ano, qual o menor e o maior valor arrecadado da exportação?
- Considerando o período de 2012 a 2023, qual a média mensal de arrecadamento com a exportação.
- Considerando o período de 2012 a 2023, qual ano teve o menor arrecadamento? E o maior?
'''

def resolucao():
    # GET DATAS
    df_etanol = pd.read_csv("https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/ie/etanol/importacoes-exportacoes-etanol-2012-2023.csv", sep=';')
    filtro_df_tipo_produto = (df_etanol['OPERAÇÃO COMERCIAL'] == 'EXPORTAÇÃO') & (df_etanol['PRODUTO'] == 'ETANOL HIDRATADO')
    df_etanol = df_etanol.loc[filtro_df_tipo_produto]



    dados_por_ano = []

    # Questão 01
    print("\nQUESTÃO 01")
    for ano_df in range(2012, 2024):
        filtro_df_ano_exportacao = (df_etanol['ANO'] == ano_df)
        df_etanol_variavel = df_etanol.loc[filtro_df_ano_exportacao]
        
        print(f'\nAno = {ano_df}')
        maior = df_etanol_variavel['DISPÊNDIO / RECEITA'].max()
        print(f"A maior foi: {maior}")

        menor = df_etanol_variavel['DISPÊNDIO / RECEITA'].min()
        print(f"A menor foi: {menor}")
        dados_por_ano.append((ano_df, maior, menor))
        print("-----------")

    # Questão 02
    print("\nQUESTÃO 02")
    print(f"Media mensal de arrecadação de 2012 a 2023: {df_etanol['DISPÊNDIO / RECEITA'].mean()}")
    
    # Questão 03
    print("\nQUESTÃO 03")
    df_resumo_por_ano = pd.DataFrame(dados_por_ano,columns=['ANO', 'MAX', 'MIN',])
    print(df_resumo_por_ano)


    filtro_coluna_max = df_resumo_por_ano['MAX'].idxmax()
    print("\nAno com maior arrecadação: ")
    print(df_resumo_por_ano.loc[filtro_coluna_max]['ANO'])

    filtro_coluna_min = df_resumo_por_ano['MIN'].idxmin()
    print("Ano com menor arrecadação: ")
    print(df_resumo_por_ano.loc[filtro_coluna_min]['ANO'])


resolucao()