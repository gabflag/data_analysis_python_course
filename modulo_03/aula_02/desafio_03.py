'''
Muitos sistemas disponilizam as informações por meio de uma API (interface de
programação de aplicações), as quais utilizam arquivos JSON (notação de objetos
JavaScript) para disponibilizar os dados. Um arquivo JSON é composto por
elementos na forma chave-valor, o que torna esse formato leve de ser transferido
e fácil de ser manipulado.

Como desenvolvedor em uma empresa de consultoria, você foi alocado para atender
um cliente que organiza processos seletivos (concurso público, vestibular,
etc.). Essa empresa possui um sistema web no qual os candidatos de um certo
processo seletivo fazem a inscrição e acompanham as informações. Um determinado
concurso precisou ser adiado, razão pela qual um processo no servidor começou a
enviar e-mails para todos os candidatos inscritos. Porém, em virtude da grande
quantidade de acessos, o servidor e a API saíram do ar por alguns segundos, o
que gerou um rompimento na criação do arquivo JSON com a lista dos candidatos já
avisados da alteração.

Por causa do rompimento do arquivo, foram gerados dois novos arquivos, razão
pela qual, desde então, não se sabe nem quem nem quantas pessoas já receberam o
aviso. Seu trabalho, neste caso, é criar uma função que, com base nas
informações que lhe serão fornecidas, retorne uma lista com os e-mails que ainda
precisam ser enviados.

Para esse projeto, você e mais um desenvolvedor foram alocados. Enquanto seu
colega trabalha na extração dos dados da API, você cria a lógica para gerar a
função. Foi combinado, entre vocês, que o programa receberá dois dicionários
referentes aos dois arquivos que foram gerados. O dicionário terá a seguinte
estrutura: três chaves (nome, email, enviado), cada uma das quais recebe uma
lista de informações; ou seja, as chaves nome e email estarão, respectivamente,
associadas a uma lista de nomes e uma de emails. por sua vez, a chave enviado
estará associada a uma lista de valores booleanos (True-False) que indicará se o
e-mail já foi ou não enviado.

Veja um exemplo.

dict_1 = {
  'nome': ['nome_1'],
  'email': ['email_1'],
  'enviado': [False]
}

Considerando que você receberá duas estruturas, conforme foi mencionado, crie
uma função que trate os dados e retorne uma lista com os e-mails que ainda não
foram enviados.

'''

def resolucao(dados_1, dados_2):
    dados_finais = {'nome': [], 'email': []}
    lista_de_envios = [dados_1, dados_2]

    for lista in lista_de_envios:
        for i, enviado in enumerate(lista['enviado']):
            if enviado == False:
                dados_finais['nome'].append(lista['nome'][i])
                dados_finais['email'].append(lista['email'][i])


    print(dados_finais['email'])


def quebrar_linhas(texto, largura=80):
    paragrafos = texto.split('\n')
    linhas_quebradas = []

    for paragrafo in paragrafos:
        palavras = paragrafo.split()
        linha_atual = ""

        for palavra in palavras:
            if len(linha_atual) + len(palavra) <= largura:
                linha_atual += palavra + " "
            else:
                linhas_quebradas.append(linha_atual.rstrip())
                linha_atual = palavra + " "

        if linha_atual:
            linhas_quebradas.append(linha_atual.rstrip())

    return '\n'.join(linhas_quebradas)

dados_1 = {
    'nome': ['Sonia Weber', 'Daryl Lowe', 'Vernon Carroll', 'Basil Gilliam', 'Mechelle Cobb', 'Edan Booker', 'Igor Wyatt', 'Ethan Franklin', 'Reed Williamson', 'Price Singleton'],
    'email': ['Lorem.ipsum@cursusvestibulumMauris.com', 'auctor@magnis.org', 'at@magnaUttincidunt.org', 'mauris.sagittis@sem.com', 'nec.euismod.in@mattis.co.uk', 'egestas@massaMaurisvestibulum.edu', 'semper.auctor.Mauris@Crasdolordolor.edu', 'risus.Quisque@condimentum.com', 'Donec@nislMaecenasmalesuada.net', 'Aenean.gravida@atrisus.edu'],
    'enviado': [False, False, False, False, False, False, False, True, False, False]
}


dados_2 = {
    'nome': ['Travis Shepherd', 'Hoyt Glass', 'Jennifer Aguirre', 'Cassady Ayers', 'Colin Myers', 'Herrod Curtis', 'Cecilia Park', 'Hop Byrd', 'Beatrice Silva', 'Alden Morales'],
    'email': ['at@sed.org', 'ac.arcu.Nunc@auctor.edu', 'nunc.Quisque.ornare@nibhAliquam.co.uk', 'non.arcu@mauriseu.com', 'fringilla.cursus.purus@erategetipsum.ca', 'Fusce.fermentum@tellus.co.uk', 'dolor.tempus.non@ipsum.net', 'blandit.congue.In@libero.com', 'nec.tempus.mauris@Suspendisse.com', 'felis@urnaconvalliserat.org'],
    'enviado': [False, False, False, True, True, True, False, True, True, False]
}

# resolucao(dados_1, dados_2)


texto = '''
'''

print(quebrar_linhas(texto))
