import pandas as pd
import matplotlib.pyplot as plt

def pandas_e_plots():
    
    myDictionary = {
        'turma' : ['A', 'B', 'C'],
        'qnt_aluno' : [22, 44, 10]        
    }

    dataframe = pd.DataFrame(myDictionary)
    print(dataframe)

    #A partir de um DataFrame, podemos invocar o método: df.plot(*args, **kwargs) para criar os gráficos. O tipo de gráfico escolhido é o 'bar'
    #dataframe.plot(x='turma', y='qnt_aluno', kind='barh')
    #dataframe.plot(x='turma', y='qnt_aluno', kind='bar')
    dataframe.plot(x='turma', y='qnt_aluno', kind='line')
    
    #Vale ressaltar que para todos os gráficos criados, a biblioteca oferece uma segunda opção de sintaxe, que é invocar o tipo de gráfico como método, por exemplo:
    #dataframe.plot.bar(x='turma', y='qnt_aluno')

    #dataframe.plot(x='turma', y='qnt_aluno', kind='pie')
    plt.show()


pandas_e_plots()