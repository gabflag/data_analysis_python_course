

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
    pass

#textos()
#trabalhando_listas()
#funcao_map()
#funcao_filter()
#trabalhando_tuplas()
objetos_set()