import seaborn as sns
import matplotlib.pyplot as plt


def seaborn_apresentacao():
    # Importando dados fake com o seaborn
    sns.set(style="whitegrid")
    df_tips = sns.load_dataset('tips')

    print(df_tips.info())
    print(df_tips.head())

    # Funcao barplot do seaborn
    fig, ax = plt.subplots(1, 3, figsize=(15, 5))

    sns.barplot(data=df_tips, x='sex', y='total_bill', ax=ax[0])
    sns.barplot(data=df_tips, x='sex', y='total_bill', ax=ax[1], estimator=sum)
    sns.barplot(data=df_tips, x='sex', y='total_bill', ax=ax[2], estimator=len)
    
    plt.show()
    
def seaborn_01():
    '''
    numero de vendas por dia
    '''
    sns.set(style="whitegrid")
    df_tips = sns.load_dataset('tips')
    
    plt.figure(figsize=(10, 5))

    ax = sns.barplot(x="day", y="total_bill", data=df_tips)

    ax.axes.set_title("Venda média diária", fontsize=14)
    ax.set_xlabel("Dia", fontsize=14)
    ax.set_ylabel("Venda média ", fontsize=14)
    ax.tick_params(labelsize=14)
        
    plt.show()


def seaborn_02():
    '''
    numero de vendas e divido por sexo
    '''
    sns.set(style="whitegrid")
    df_tips = sns.load_dataset('tips')
    
    plt.figure(figsize=(10, 5))
    sns.countplot(data=df_tips, x="day", hue="sex")
            
    plt.show()


def seaborn_03():
    '''
    Vamos construir um gráfico que permita avaliar se existe uma relação 
    entre o valor da conta e da gorjeta. Será que quem gastou mais também deu mais gorjeta? 
    '''
    sns.set(style="whitegrid")
    df_tips = sns.load_dataset('tips')
    
    plt.figure(figsize=(10, 5))
    sns.scatterplot(data=df_tips, x="total_bill", y="tip")

    '''
    Olhando para o gráfico, parece quanto maior o valor da conta,
    maior foi o valor da gorjeta. Esse comportamento é chamado de relação linear, 
    pois conseguimos traçar uma reta entre os pontos, descrevendo seu 
    comportamento através de uma função linear.
    
    é o mais legal...
    gráfico scatterplot é muito utilizado por cientistas de dados que estão buscando por padrões nos dados.
    '''
            
    plt.show()

seaborn_03()
