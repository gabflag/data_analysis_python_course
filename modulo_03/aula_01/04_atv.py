#  a função keys() retorna uma lista com todas as chaves de um dicionário. 
# A função values() retorna uma lista com todos os valores. 
# A função items() retorna uma lista de tuplas, cada uma das quais é um par chave-valor

def trabalhando_dici():
    cadastro = {
                'nome' : ['João', 'Ana', 'Pedro', 'Marcela'],
                'cidade' : ['São Paulo', 'São Paulo', 'Rio de Janeiro', 'Curitiba'],
                'idade' : [25, 33, 37, 18]
                }
    
    print(f"Quantidade de chaves: {len(cadastro)}") # Retorna 3

    print(f"Usando a função key: {cadastro.keys()}") #  retorna uma lista com todas as chaves no dicionário.
    print(f"Usando a função values: {cadastro.values()}") # retorna uma lista com os valores. Como os valores também são listas, temos uma lista de listas.
    print(f"Usando a função items: {cadastro.items()}") # cadastro.items(): retorna uma lista de tuplas, cada uma das quais é composta pela chave e pelo valor.


    print("\n cadastro['nome'] = ", cadastro['nome'])
    print("\n cadastro['nome'][2] = ", cadastro['nome'][2])
    print("\n cadastro['idade'][2:] = ", cadastro['idade'][2:])

    print(len(cadastro['nome']))
    print(len(cadastro['cidade']))
    print(len(cadastro['idade']))

    # soma de uma lista de um criada a partir de um laço for (cahve assume o valor das chaves do dici)
    qtde_itens = sum([len(cadastro[chave]) for chave in cadastro])
    print(f"\n\nQuantidade de elementos no dicionário = {qtde_itens}")

trabalhando_dici()