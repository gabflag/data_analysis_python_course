'''
Como desenvolvedor em uma empresa de consultoria, você continua alocado para
atender um cliente que precisa fazer a ingestão de dados de uma nova fonte e
tratá-las. Você já fez uma entrega na qual implementou uma solução que faz o
dedup em uma lista de CPFs, retorna somente a parte numérica do CPF e verifica
se eles possuem 11 dígitos.

Os clientes aprovaram a solução, mas solicitaram que a lista de CPFs válidos
fosse entregue em ordem crescente para facilitar o cadastro. Eles enfatizaram a
necessidade de ter uma solução capaz de fazer o trabalho para grandes volumes de
dados, no melhor tempo possível. Uma vez que a lista de CPFs pode crescer
exponencialmente, escolher os algoritmos mais adequados é importante nesse caso.

Portanto, nesta nova etapa, você deve tanto fazer as transformações de limpeza e
validação nos CPFs (remover ponto e traço, verificar se tem 11 dígitos e não
deixar valores duplicados) quanto fazer a entrega em ordem crescente. Quais
algoritmos você vai escolher para implementar a solução? Você deve apresentar
evidências de que fez a escolha certa!
'''

def executar_merge_sort(lista, inicio=0, fim=None):
    if not fim:
        fim = len(lista)
        
    if fim - inicio > 1:
        meio = (inicio + fim) // 2
        executar_merge_sort(lista, inicio, meio)
        executar_merge_sort(lista, meio, fim)
        executar_merge(lista, inicio, meio, fim)
    return lista


def executar_merge(lista, inicio, meio, fim):
    esquerda = lista[inicio:meio]
    direita = lista[meio:fim]
    topo_esquerda = topo_direita = 0
    for p in range(inicio, fim):
        if topo_esquerda >= len(esquerda):
            lista[p] = direita[topo_direita]
            topo_direita += 1
        elif topo_direita >= len(direita):
            lista[p] = esquerda[topo_esquerda]
            topo_esquerda += 1
        elif esquerda[topo_esquerda] < direita[topo_direita]:
            lista[p] = esquerda[topo_esquerda]
            topo_esquerda += 1
        else:
            lista[p] = direita[topo_direita]
            topo_direita += 1 


def limpar_cpfs(lista_cpf):
    cpf_limpo = []
    for cpf in lista_cpf:
        lista_remocao = [" ", ".", ",", "(", ")", "-"]
        for caractere in lista_remocao:
            cpf = cpf.replace(caractere, "")
        cpf_limpo.append(cpf)

    return cpf_limpo  


lista_cpfs = ['44444444444', '111.111.111-11', '11111111111', '222.222.222-22', '333.333.333-33', '22222222222', '444.44444']
cpfs_limpos = limpar_cpfs(lista_cpfs)

lista_organizada_com_merge = executar_merge_sort(cpfs_limpos)
print(lista_organizada_com_merge)