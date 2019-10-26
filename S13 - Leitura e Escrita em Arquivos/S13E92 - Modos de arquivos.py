"""
Modos de arquivos

r -> Abre para leitura - default
w -> Abre para escrita - Sobre-escreve caso o arquivo já exista
x -> Abre para escrita somente se o arquivo não existir, caso o arquivo já existe ocorre FileExistsError
+ -> Abre para o modo de atualização - Leitura e Escrita

http://docs.python.org/3/library/functions.html#open

#exemplo com modo x
try:
    with open('university.txt', 'x') as arquivo:
        arquivo.write('Teste do modo x de conteudo.\n')
except FileExistsError:
    print('Arquivo já existe.')

#exemplo com modo a - Caso o arquivo não exista ele cria o arquivo, caso contrário ele adiciona as informações após a ultima linha sempre

with open('frutas.txt', 'a') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou sair :')
        if fruta != 'sair':
            arquivo.write(f'Fruta: {fruta} \n')
        else:
            break

#exemplo com modo a - tentando escrever na primeira linha as informações

with open('outro.txt', 'a') as arquivo:
    arquivo.seek(0)
    arquivo.write('Topo.\n')
    arquivo.write('Nova Linha.\n')
    arquivo.write('Mais uma linha.')


Com o modo a não é possível controlar o cursor

"""

with open('outro.txt', 'a+') as arquivo:
    arquivo.seek(0)
    arquivo.write('Toposss.\n')
    arquivo.write('Nova Linha.\n')



