from matplotlib import pyplot as plt
import random
import numpy as np


def primeira_licao():
    # Lista com vetores aleatórios
    dados01 = random.sample(range(100), k=20)
    dados02 = random.sample(range(100), k=20)

    plt.plot(dados01, dados02)
    '''
    plt.xlabel('Dados 01')
    plt.ylabel('Dados 02')
    plt.title('Gráfico de Dados Aleatórios')
    '''
    plt.show()


def figura_com_eixo_variavel():

    x = range(5)
    x = np.array(x) # temos que converter para um array numpy, senão o plot não consegue fazer operações.

    # Cria uma figura com uma única linha e dois subplots (eixos) que serão armazenados na matriz ax.
    figura, ax = plt.subplots(1, 2, figsize=(12, 5))

    print("Tipo de ax = ", type(ax))
    print("Conteudo de ax[0] = ", ax[0])
    print("Conteudo de ax[1] = ", ax[1])

    # Preenchendo a primeira figura:
    ax[0].plot(x, x, label='X normal')
    ax[0].plot(x, x ** 2, label='X vezes 2')
    ax[0].plot(x, x ** 3, label='X vezes 3')

    ax[0].set_xlabel('Eixo X')
    ax[0].set_ylabel('Eixo Y')
    ax[0].set_title('Gráfico 01')
    ax[0].legend()


    ax[1].plot(x, x, 'r--', label='X normal')
    ax[1].plot(x ** 2, x, 'g--', label='X vezes 2')
    ax[1].plot(x ** 3, x, 'b--', label='X vezes 3')
    ax[1].set_xlabel('Eixo X')
    ax[1].set_ylabel('Eixo Y')
    ax[1].set_title('Gráfico 02')
    ax[1].legend()
    
    plt.show()


def figura_sem_eixo_variavel():
    '''
    Muda basicamente o método de criação
    '''
    x = range(5)
    x = np.array(x)

    figura = plt.subplots(figsize=(12, 5))
    plt.subplot(121) # Adiciona um grid de subplots a figura: 1 linha, 2 colunas - Figura 1   

    plt.plot(x, x, label='X normal')
    plt.plot(x, x ** 2, label='X vezes 2')
    plt.plot(x, x ** 3, label='X vezes 3')
    plt.title("Gráfico 1")
    plt.xlabel('Eixo x')
    plt.ylabel('Eixo y')
    plt.legend()


    plt.subplot(122) # Adiciona um grid de subplots a figura: 1 linha, 2 colunas - Figura 2            
    plt.plot(x, x, 'r--', label='X normal')
    plt.plot(x**2, x, 'b--',label='X vezes 2')
    plt.plot(x**3, x, 'g--', label='X vezes 3')
    plt.title("Gráfico 2")
    plt.xlabel('Novo eixo x')
    plt.ylabel('Novo eixo y')
    plt.legend()

    plt.show()

figura_sem_eixo_variavel()