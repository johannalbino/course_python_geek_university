"""
Escrevendo em arquivos

OBS:
Ao abrir um arquivo para leitura, não podemos realizar a escrita neste arquivo, apenas leitura.
Da mesma forma, se abrirmos um arquivo para escrita, não podemos lê-lo, somente escrever nele.

Para escrevermos dados em um arquivo após abrir o arquivo utilizamos a função write().
Esta função recebe uma string como parâmetro, caso contrario teremos TypeError

#Exemplo de escrita - mode w

with open('novo.txt', 'w') as arquivo:
    arquivo.write('Escrever dados em arquivos é muito fácil.\n')
    arquivo.write('Podemos colocar quantas linhas quisermos.\n')
    arquivo.write('Está é a ultima linha.')

#Exemplo de escrita - mode w - Sobrescreve o arquivo ou cria um novo arquivo

with open('novo.txt', 'w') as arquivo:
    arquivo.write('Novos dados.\n')
    arquivo.write('Outro que podemos colocar quantas linhas quisermos.\n')
    arquivo.write('Está é a ultima linha.')

# Forma não Pythonica


arquivo = open('novo.txt', 'w')
arquivo.write('Um texto qualquer.\n')
arquivo.write('Mais um texto.\n')
arquivo.close()

with open('geek.txt', 'w') as arquivo:
    arquivo.write('Geek\n' * 1000)

"""
with open('frutas.txt', 'w') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou digite sair:')
        if fruta != 'sair':
            arquivo.write(f'Fruta: {fruta} \n')
        else:
            break
