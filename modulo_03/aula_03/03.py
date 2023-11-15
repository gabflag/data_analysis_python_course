# ALGORITMOS DE ORDENAÇÃO


# Complexidade O(N2): neste grupo estão os algoritmos selection sort, bubble sort
# e insertion sort. Esses algoritmos são lentos para ordenação de grandes listas,
# porém são mais intuitivos de entender e possuem uma codificação mais simples.

# Complexidade O(N log N): deste grupo, vamos estudar os algoritmos merge sort e
# quick sort. Tais algoritmos possuem performance superior, porém são um pouco
# mais complexos de serem implementados.


# Para finalizar nossa aula, vale ressaltar que a performance de cada algoritmo
# vai depender da posição do valor na lista e do seu tamanho. Por exemplo, no
# algoritmo insertion sort, dado que o lado esquerdo é conhecido (e ordenado), se
# o valor a ser inserido é grande, o algoritmo terá uma boa performance. Por outro
# lado, o algoritmo selection sort, uma vez que verifica o mínimo para frente, que
# não se conhece, sempre está no pior caso.


def busca_binaria():
    # Existem duas formas já programadas que nos permitem ordenar uma sequência: 
    # a função built-in sorted() e o método sort(), presente nos objetos da classe list.
    lista = [10, 4, 1, 15, -3]

    lista_ordenada1 = sorted(lista)
    lista_ordenada2 = lista.sort()

    print('lista = ', lista, '\n')
    print('lista_ordenada1 = ', lista_ordenada1)
    print('lista_ordenada2 = ', lista_ordenada2) #  faz a ordenação "inplace" (ou seja, dentro da própria lista passada como parâmetro). 
    print('lista = ', lista)

    print("\n##############")
    print("Outros métodos de ordenação: ")
    lista = [7, 4]
    if lista[0] > lista[1]:
        aux = lista[1]
        lista[1] = lista[0]
        lista[0] = aux

    print(lista)


    print("\n##############")
    lista = [5, -1]

    if lista[0] > lista[1]:
        lista[0], lista[1] = lista[1], lista[0]

    print(lista)


def selection_sort():
    '''
    O algoritmo selection sort recebe esse nome, porque faz a ordenação sempre
    escolhendo o menor valor para ocupar uma determinada posição. Para entendermos
    como funciona o algoritmo, suponha que exista uma fila de pessoas, mas que, por
    algum motivo, elas precisem ser colocadas por ordem de tamanho, do menor para o
    maior. Essa ordenação será feita por um supervisor. Segundo o algoritmo
    selection sort, esse supervisor olhará para cada uma das pessoas na fila e
    procurará a menor delas. Quando encontrá-la, essa pessoa trocará de posição com
    a primeira. Veja que, agora, a primeira pessoa da fila está na posição correta,
    pois é a menor. Em seguida, o supervisor precisa olhar para as demais e escolher
    a segunda menor pessoa; quando encontrá-la, a pessoa troca de lugar com a
    segunda. Agora as duas primeiras pessoas da fila estão ordenadas. Esse mecanismo
    é feito até que todos estejam em suas devidas posições. Portanto, a lógica do
    algoritmo é a seguinte:
        
        -Iteração 1: percorre toda a lista, procurando o menor valor para ocupar a
        posição 0.
        - Iteração 2: a partir da posição 1, percorre toda a lista, procurando o menor
        valor para ocupar a posição 1.
        - Iteração 3: a partir da posição 2, percorre toda a lista, procurando o menor
        valor para ocupar a posição 2.
        - Esse processo é repetido N-1 vezes, sendo N o tamanho da lista.
    '''
    lista = [10, 9, 5, 8, 11, -1, 3]
    n = len(lista)
    
    for i in range(0, n):
        index_menor = i
        for j in range(i+1, n):
            if lista[j] < lista[index_menor]:
                index_menor = j
        lista[i], lista[index_menor] = lista[index_menor], lista[i]
    print(lista)

    #OR
    
    lista_ordenada = []
    while lista:
        minimo = min(lista)
        lista_ordenada.append(minimo)
        lista.remove(minimo)
    print(lista_ordenada)


def bubble_sort():
    '''
    O algoritmo bubble sort (algoritmo da bolha) recebe esse nome porque faz a
    ordenação sempre a partir do ínicio da lista, comparando um valor com seu
    vizinho. Para entendermos como funciona o algoritmo, suponha que exista uma fila
    de pessoas, mas que, por algum motivo, elas precisem ser colocadas por ordem de
    tamanho, do menor para o maior. Segundo o algoritmo bubble sort, a primeira
    pessoa da fila (pessoa A), perguntará para o segundo a altura – se o segundo for
    menor, então eles trocam de lugar. Novamente, a pessoa A perguntará para seu
    próximo vizinho qual é a altura deste – se esta for menor, eles trocam. Esse
    processo é repetido até que a pessoa A encontre alguém que é maior, contexto no
    qual essa nova pessoa vai percorrer a fila até o final fazendo a mesma pergunta.
    Esse processo é repetido até que todas as pessoas estejam na posição correta. A
    lógica do algoritmo é a seguinte:
     
        - Iteração 1: seleciona o valor na posição 0 e o compara com seu vizinho – se for
        menor, há troca; se não for, seleciona o próximo e compara, repentindo o
        processo.
        - Iteração 2: seleciona o valor na posição 0 e compara ele com seu vizinho, se for
        menor troca, senão seleciona o próximo e compara, repentindo o processo.
        - Iteração N - 1: seleciona o valor na posição 0 e o compara com seu vizinho – se
        for menor, há troca; se não for, seleciona o próximo e compara, repentindo o
        processo.
    
    '''
    lista = [10, 9, 5, 8, 11, -1, 3]
    n = len(lista)
    for i in range(n-1):
        for j in range(n-1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    print(lista)


def insertion_sort():
    '''
    O algoritmo insertion sort (algoritmo de inserção) recebe esse nome porque faz a
    ordenação pela simulação da inserção de novos valores na lista. Para entendermos
    como funciona o algoritmo, imagine um jogo de cartas para a execução do qual
    cada jogador começa com cinco cartas e, a cada rodada, deve pegar e inserir uma
    nova carta na mão. Para facilitar, o jogador opta por deixar as cartas ordenadas
    em sua mão, razão pela qual, a cada nova carta que precisar inserir, ele olha a
    sequência da esquerda para a direita, procurando a posição exata para fazer a
    inserção. A lógica do algoritmo é a seguinte:

        Início: parte-se do princípio de que a lista possui um único valor e,
        consequentemente, está ordenada.
        Iteração 1: parte-se do princípio de que um novo valor precisa ser inserido na
        lista; nesse caso, ele é comparado com o valor já existente para saber se
        precisa ser feita uma troca de posição.
        Iteração 2: parte-se do princípio de que um novo valor precisa ser inserido na
        lista; nesse caso, ele é comparado com os valores já existentes para saber se
        precisam ser feitas trocas de posição.
        Iteração N: parte-se do princípio de que um novo valor precisa ser inserido na
        lista; nesse caso, ele é comparado com todos os valores já existentes (desde o
        início) para saber se precisam ser feitas trocas de posição.
    '''
    
    lista = [10, 9, 5, 8, 11, -1, 3]
    n = len(lista)

    for i in range(1, n):
        valor_inserir = lista[i] 
        j = i - 1
        
        while j >= 0 and lista[j] > valor_inserir:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = valor_inserir
    
    return lista


def executar_merge(esquerda, direita):
    sub_lista_ordenada = []
    topo_esquerda, topo_direita = 0, 0
    while topo_esquerda < len(esquerda) and topo_direita < len(direita):
        if esquerda[topo_esquerda] <= direita[topo_direita]:
            sub_lista_ordenada.append(esquerda[topo_esquerda])
            topo_esquerda += 1
        else:
            sub_lista_ordenada.append(direita[topo_direita])
            topo_direita += 1
    sub_lista_ordenada += esquerda[topo_esquerda:]
    sub_lista_ordenada += direita[topo_direita:]
    return sub_lista_ordenada


def executar_merge_sort(lista):
    if len(lista) <= 1: return lista
    else:
        meio = len(lista) // 2
        esquerda = executar_merge_sort(lista[:meio])
        direita = executar_merge_sort(lista[meio:])
        return executar_merge(esquerda, direita)

    
def executar_merge(esquerda, direita):
    '''
    O algoritmo merge sort recebe esse nome porque faz a ordenação em duas etapa:
    (i) divide a lista em sublistas; e (ii) junta (merge) as sublistas já ordenadas.
    Esse algoritmo é conhecido por usar a estratégia "dividir para conquistar"
    (STEPHENS, 2013). Essa estratégia é usada por algoritmos de estrutura recursiva:
    para resolver um determinado problema, eles se chamam recursivamente uma ou mais
    vezes para lidar com subproblemas intimamente relacionados. Esses algoritmos
    geralmente seguem uma abordagem de dividir e conquistar: eles dividem o problema
    em vários subproblemas semelhantes ao problema original, mas menores em tamanho,
    resolvem os subproblemas recursivamente e depois combinam essas soluções para
    criar uma solução para o problema original (CORMEN et al., 2001). O paradigma de
    dividir e conquistar envolve três etapas em cada nível da recursão: (i) dividir
    o problema em vários subproblemas; (ii) conquistar os subproblemas,
    resolvendo-os recursivamente – se os tamanhos dos subproblemas forem pequenos o
    suficiente, apenas resolva os subproblemas de maneira direta; (iii) combine as
    soluções dos subproblemas na solução do problema original.
        Etapa de divisão:
            Com base na lista original, encontre o meio e separe-a em duas listas:
            esquerda_1 e direita_2.
            Com base na sublista esquerda_1, se a quantidade de elementos for maior que 1,
            encontre o meio e separe-a em duas listas: esquerda_1_1 e direta_1_1.
            Com base na sublista esquerda_1_1, se a quantidade de elementos for maior que 1,
            encontre o meio e separe-a em duas listas: esquerda_1_2 e direta_1_2.
            Repita o processo até encontrar uma lista com tamanho 1.
            Chame a etapa de merge.
            Repita o processo para todas as sublistas.
    
    Para entender a etapa de junção do merge sort, suponha que você está vendo duas
    fileiras de crianças em ordem de tamanho. Ao olhar para a primeira criança de
    cada fila, é possível identificar qual é a menor e, então, colocá-la na posição
    correta. Fazendo isso sucessivamente, teremos uma fila ordenada com base nas
    duas anteriores.
        Etapa de merge:
            Dadas duas listas, cada uma das quais contém 1 valor – para ordenar, basta
            comparar esses valores e fazer a troca, gerando uma sublista com dois valores
            ordenados.
            Dadas duas listas, cada uma das quais contém 2 valores – para ordenar, basta ir
            escolhendo o menor valor em cada uma e gerar uma sublista com quatro valores
            ordenados.
            Repita o processo de comparação e junção dos valores até chegar à lista
            original, agora ordenada.

    '''
    sub_lista_ordenada = []
    topo_esquerda, topo_direita = 0, 0
    while topo_esquerda < len(esquerda) and topo_direita < len(direita):
        if esquerda[topo_esquerda] <= direita[topo_direita]:
            sub_lista_ordenada.append(esquerda[topo_esquerda])
            topo_esquerda += 1
        else:
            sub_lista_ordenada.append(direita[topo_direita])
            topo_direita += 1
    sub_lista_ordenada += esquerda[topo_esquerda:]
    sub_lista_ordenada += direita[topo_direita:]
    return sub_lista_ordenada


def executar_quicksort(lista, inicio, fim):
    if inicio < fim:
        pivo = executar_particao(lista, inicio, fim)
        executar_quicksort(lista, inicio, pivo-1)
        executar_quicksort(lista, pivo+1, fim)
    return lista

        
def executar_particao(lista, inicio, fim):
    pivo = lista[fim]
    esquerda = inicio
    for direita in range(inicio, fim):
        if lista[direita] <= pivo:
            lista[direita], lista[esquerda] = lista[esquerda], lista[direita]
            esquerda += 1
    lista[esquerda], lista[fim] = lista[fim], lista[esquerda]
    return esquerda


def executar_quicksort_2(lista):
    # recursivamente até que a lista esteja ordenada.
    if len(lista) <= 1: return lista    
    pivo = lista[0]
    iguais  = [valor for valor in lista if valor == pivo]
    menores = [valor for valor in lista if valor <  pivo]
    maiores = [valor for valor in lista if valor >  pivo]
    return executar_quicksort_2(menores) + iguais + executar_quicksort_2(maiores)



lista = [10, 9, 5, 8, 11, -1, 3]
#busca_binaria()
#selection_sort()
#bubble_sort()
#insertion_sort()
#print(executar_merge_sort(lista))
#print(executar_quicksort_2(lista))