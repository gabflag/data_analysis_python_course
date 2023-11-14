Como desenvolvedor em uma empresa de consultoria de software, você foi alocado em um projeto para uma empresa de geração de energia.
Essa empresa tem interesse em criar uma solução que acompanhe as exportações de etanol no Brasil. Esse tipo de informação está 
disponível no site do governo brasileiro http://www.dados.gov.br/dataset, em formatos CSV, JSON, dentre outros.

No endereço http://www.dados.gov.br/dataset/importacoes-e-exportacoes-de-etanol é possível encontrar várias bases de dados (datasets), 
contendo informações de importação e exportação de etanol. O cliente está interessado em obter informações sobre a Exportação Etano
Hidratado (barris equivalentes de petróleo) 2012-2020, cujo endereço é http://www.dados.gov.br/dataset/importacoes-e-exportacoes-de-etanol/resource/ca6a2afe-def5-4986-babc-b5e9875d39a5.
Para a análise será necessário fazer o download do arquivo.

O cliente deseja uma solução que extraia as seguintes informações:

- Em cada ano, qual o menor e o maior valor arrecadado da exportação?
- Considerando o período de 2012 a 2019, qual a média mensal de arrecadamento com a exportação.
- Considerando o período de 2012 a 2019, qual ano teve o menor arrecadamento? E o maior?

Como parte das informações técnicas sobre o arquivo, foi lhe informado que se trata de um arquivo delimitado CSV, cujo separador de campos é 
ponto-e-vírgula e a codificação do arquivo está em ISO-8859-1. Como podemos obter o arquivo? Como podemos extrair essas informações 
usando a linguagem Python? Serão necessários transformações nos dados para obtermos as informações solicitadas?

# Link mais atualizado para o desafio:
# https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/ie/etanol/importacoes-exportacoes-etanol-2012-2023.csv