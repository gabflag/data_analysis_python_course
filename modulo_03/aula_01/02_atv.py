def atv_01():
    '''
    Dado um texto sobre strings em Python, queremos saber quantas vezes o autor menciona a palavra string ou strings.
    '''

    texto = """Operadores de String
    Python oferece operadores para processar texto (ou seja, valores de string).
    Assim como os números, as strings podem ser comparadas usando operadores de comparação:
    ==, !=, <, > e assim por diante.
    O operador ==, por exemplo, retorna True se as strings nos dois lados do operador tiverem o mesmo valor (Perkovic, p. 23, 2016).
    """

    palavras = texto.split()
    total = 0
    for palavra in palavras:
        lista_remocao = [" ", ".", ",", "(", ")"]
        for regra in lista_remocao:
            palavra = palavra.replace(regra, "")
        
        if palavra.lower() == "string" or palavra.lower() == "strings":
            total+=1

    print(total)

atv_01()