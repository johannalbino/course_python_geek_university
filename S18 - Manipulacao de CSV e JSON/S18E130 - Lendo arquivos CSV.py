""""
Lendo arquivos CSV

CSV -> Comma Separeted Values - Valores separados por Vírgula

# Separado por Vírgula
1, 2, 3, 4, 5, 6
"geek", "university", "python", "ciência", "dados

# Separado por Ponto e Vírgula
1; 2; 3; 4; 5; 6
"geek"; "university"; "python"; "ciência"; "dados

# Separado por Espaço
1 2 3 4 5 6
"geek" "university" "python" "ciência" "dados


http://dados.gov.br/dataset

#Não é a forma ideal para se trabalhar com CSV

with open('lutadores.csv', encoding="utf8") as arquivo:
    dados = arquivo.read()
    dados = dados.split(',')[2:]
    print(dados)

A linguagem Python possui duas formas diferentes para ler dados em arquivos CSV
    - reader -> Permite que iteremos sobre as linhas do arquivo CSV como listas
    - DictReader -> Permite que iteremos sobre as linhas do arquivo CSV como OrderedDicts


#Exemplo Reader
from csv import reader

with open('lutadores.csv', encoding='utf8') as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv)
    for linha in leitor_csv:
        print(f'{linha[0]} nasceu no(a)(s) {linha[1]} e mede {linha[2]}')
        print(linha)
"""
#Exemplo DictReader

from csv import DictReader

with open('lutadores.csv', encoding='utf8') as arquivo:
    leitor_csv = DictReader(arquivo, delimiter=',')
    for linha in leitor_csv:
        print(f"{linha['Nome']} nasceu no(a) {linha['País']} e mede {linha['Altura (em cm)']}")
