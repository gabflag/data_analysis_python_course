import numpy

#Objetos do tipo sequência: texto, listas e tuplas.
def textos():
    texto = "Aprendendo Python na disciplina de linguagem de programação."

    print(f"Tamanho do texto = {len(texto)}")
    print(f"Python in texto = {'Python' in texto}")
    print(f"Quantidade de y no texto = {texto.count('y')}")
    print(f"As 5 primeiras letras são: {texto[0:6]}")

    print(texto.upper())
    print(texto.replace("i", 'XX'))

    print(f"texto = {texto}")
    print(f"Tamanho do texto = {len(texto)}\n")

    palavras = texto.split()
    print(f"palavras = {palavras}")
    print(f"Tamanho de palavras = {len(palavras)}")


def trabalhando_listas():

    vogais = ['a', 'e', 'i', 'o', 'u']

    for vogal in vogais:
        print (f'Posição = {vogais.index(vogal)}, valor = {vogal}')


    frutas = ["maça", "banana", "uva", "mamão", "maça"]
    notas = [8.7, 5.2, 10, 3.5]

    print("maça" in frutas) # True
    print("abacate" in frutas) # False
    print("abacate" not in frutas) # True
    print(min(frutas)) # banana
    print(max(notas)) # 10
    print(frutas.count("maça")) # 2
    print(frutas + notas)
    print(2 * frutas)

    print("\n# #  # # # # # # # # #")
    lista = ['Python', 30.61, "Java", 51 , ['a', 'b', 20], "maça"]

    print(f"Tamanho da lista = {len(lista)}")

    for i, item in enumerate(lista):
        print(f"Posição = {i},\t valor = {item} -----------------> tipo individual = {type(item)}")

    print("\nExemplos de slices:\n")

    print("lista[1] = ", lista[1])
    print("lista[0:2] = ", lista[0:2])
    print("lista[:2] = ", lista[:2])
    print("lista[3:5] = ", lista[3:5])
    print("lista[3:6] = ", lista[3:6])
    print("lista[3:] = ", lista[3:])
    print("lista[-2] = ", lista[-2])
    print("lista[-1] = ", lista[-1])
    print("lista[4][1] = ", lista[4][1])

    print("\n# #  # # # # # # # # #")
    # ist comprehension, também chamada de listcomp, é uma forma pythônica de criar uma lista com base em um objeto iterável

    linguagens = ["Python", "Java", "JavaScript", "C", "C#", "C++", "Swift", "Go", "Kotlin"]

    print("Antes da listcomp = ", linguagens)

    linguagens = [item.lower() for item in linguagens]

    print("\nDepois da listcomp = ", linguagens)
    
    print("\n# #  # # # # # # # # #")
    linguagens = '''Python Java JavaScript C C# C++ Swift Go Kotlin'''.split()
    linguagens_java = [item for item in linguagens if "Java" in item]
    print(linguagens_java)


def funcao_map():
    '''
    A função map() é utilizada para aplicar uma determinada função em 
    cada item de um objeto iterável. Para que essa transformação seja 
    feita, a função map() exige que sejam passados dois parâmetros: 
    a função e o objeto iterável. 
    '''

    print("Exemplo 01")
    liguagens = '''Python Java JavaScript C C# C++ Swift Go Kotlin'''.split()
    nova_lista = map(lambda x: x.lower(), liguagens)
    print(f"A nova lista é = {nova_lista}\n")
    
    # A função map retorna um objeto iterável. Para que possamos
    # ver o resultado, precisamos transformar esse objeto em uma lista
    nova_lista = list(nova_lista)
    print(f"A nova lista corretamente = {nova_lista}\n")


    # Exemplo 2
    print("\n\nExemplo 2")
    numeros = [0, 1, 2, 3, 4, 5]

    quadrados = list(map(lambda x: x*x, numeros))
    print(f"Lista com o número elevado a ele mesmo = {quadrados}\n")


def funcao_filter():
    '''
    A função filter() tem as mesmas características da função map(), mas, 
    em vez de usarmos uma função para transformar os valores da lista, 
    nós a usamos para filtrar. 
    '''
    numeros = list(range(0,21))
    numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
    print(numeros_pares)
    

def trabalhando_tuplas():
    #função enumerate é iterar sobre uma sequência (como uma lista, tupla, string, etc.)
    #e retornar tanto o índice quanto o valor do elemento durante cada iteração.
    vogais = ('a','e', 'i', 'o', 'u')
    for p, x in enumerate(vogais):
        print(f"Posição = {p}, valor = {x}")

    # OU
    print("#")
    for item in enumerate(vogais):
        print(item)


def objetos_set():
    # Um objeto do tipo set habilita operações matemáticas 
    # de conjuntos, tais como: união, intersecção, diferenteça, etc.
    # Usando um par de chaves e elementos separados por vírgulas: set1 = {'a', 'b', 'c'}
    # Usando o construtor de tipo: set(iterable)
    vogais_1 = {'aeiou'} # sem uso do construtor
    print(type(vogais_1), vogais_1)

    vogais_2 = set('aeiouaaaaaa') # construtor com string
    print(type(vogais_2), vogais_2)

    vogais_3 = set(['a', 'e', 'i', 'o', 'u']) # construtor com lista
    print(type(vogais_3), vogais_3)

    vogais_4 = set(('a', 'e', 'i', 'o', 'u')) # construtor com tupla
    print(type(vogais_4), vogais_4)

    print(set('banana'))


def objetos_mapping():
    # As estruturas de dados que possuem um mapeamento entre uma 
    # chave e um valor são consideradas objetos do tipo mapping
    # o objeto que possui essa propriedade é o dict (dicionário).
    
    # Usando um par de chaves para denotar um dict vazio: dicionario1 = {}
    # Usando um par de elementos na forma, chave : valor separados por 
    # vírgulas: dicionario2 = {'one': 1, 'two': 2, 'three': 3}
    # Usando o construtor de tipo: dict()
    
    dici_1 = {}
    dici_1['nome'] = "João"
    dici_1['idade'] = 30
    
    # Exemplo 2 - Criação de dicionário usando um par elementos na forma, chave : valor
    dici_2 = {'nome': 'João', 'idade': 30}

    # Exemplo 3 - Criação de dicionário com uma lista de tuplas. Cada tupla representa um par chave : valor
    dici_3 = dict([('nome', "João"), ('idade', 30)])

    # Exemplo 4 - Criação de dicionário com a função built-in zip() e 
    # duas listas, uma com as chaves, outra com os valores.
    # A função zip() é usada para combinar valores de diferentes sequências e retorna um iterável de tuplas
    dici_4 = dict(zip(['nome', 'idade'], ["João", 30]))

    print(dici_1 == dici_2 == dici_3 == dici_4)
    

    print(dici_2['nome'])


def objetos_arraynumpy():
    matriz_1_1 = numpy.array([1, 2, 3]) # Cria matriz 1 linha e 1 coluna
    matriz_2_2 = numpy.array([[1, 2], [3, 4]]) # Cria matriz 2 linhas e 2 colunas
    matriz_3_2 = numpy.array([[1, 2], [3, 4], [5, 6]]) # Cria matriz 3 linhas e 2 colunas
    matriz_2_3 = numpy.array([[1, 2, 3], [4, 5, 6]]) # Cria matriz 2 linhas e 3 colunas


    matriz_lista = [[1, 2, 3], [4, 5, 6]]
    print(f"A matriz feita no formato de lista: { matriz_lista}")


    print(type(matriz_1_1))

    print('\n matriz_1_1 = ', matriz_1_1)
    print('\n matriz_2_2 = \n', matriz_2_2)
    print('\n matriz_3_2 = \n', matriz_3_2)
    print('\n matriz_2_3 = \n', matriz_2_3)
    
    print("##################")
    
    m1 = numpy.zeros((3, 3)) # Cria matriz 3 x 3 somente com zero
    m2 = numpy.ones((2,2)) # Cria matriz 2 x 2 somente com um
    m3 = numpy.eye(4) # Cria matriz 4 x 4 identidade
    m4 = numpy.random.randint(low=0, high=100, size=10).reshape(2, 5) # Cria matriz 2 X 5 com números inteiros

    print('\n numpy.zeros((3, 3)) = \n', numpy.zeros((3, 3)))
    print('\n numpy.ones((2,2)) = \n', numpy.ones((2,2)))
    print('\n numpy.eye(4) = \n', numpy.eye(4))
    print('\n m4 = \n', m4)

    print(f"Soma dos valores em m4 = {m4.sum()}")
    print(f"Valor mínimo em m4 = {m4.min()}")
    print(f"Valor máximo em m4 = {m4.max()}")
    print(f"Média dos valores em m4 = {m4.mean()}")
        

#textos()
#trabalhando_listas()
#funcao_map()
#funcao_filter()
#trabalhando_tuplas()
#objetos_set()
#objetos_mapping()
objetos_arraynumpy()