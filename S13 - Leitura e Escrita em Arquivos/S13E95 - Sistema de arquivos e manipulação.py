"""

Sistema de arquivos e manipulação

import os


print(os.path.exists('arquivo.txt'))  #Verificando se o arquivo.txt existe na pasta
print(os.path.exists('texto.txt')) #Verificando se o texto.txt existe na pasta

print(os.path.exists('pasta_um')) #Verificando se a pasta pasta_um existe

#criando arquivos

#forma 1
open('arquivos-teste.txt', 'w').close()

#forma 2
open('arquivo-teste2.txt', 'a').close()

#forma 3
with open('arquivo-teste3.txt', 'w') as arquivo:
    pass

# Forma de criar arquivo em linux
os.mknod('arquivo-teste4.txt')
os.mknod('geek/university.txt')

os.mkdir('templates')

# Se o diretório já existir vai dar error FileExistsError

#Para criar um diretorio


# Para criar um diretório dentro de um que já existe

os.mkdir('templates/teste')


#Para criar uma arvore de diretorios

os.makedirs('templates2/teste/2')

# Crie o diretorio template2, caso já existir essa pasta não ocasione erro
os.makedirs('templates2', exist_ok=True)

# Renomear arquivos/diretórios

#Diretórios
os.rename('templates2','temp2')

#Arquivos
os.rename('texto.txt', 'texto2.txt')

# ATENÇÃO! Tome cuidado com os comandos de deleção. Ao deletarmos um arquivo ou diretório, eles não vão para a lixeira. Eles somem

os.remove('arquivos-teste.txt')

# Caso o arquivo não exista, teremos o FileNotFoundError
# No windows se o arquivo estiver aberto terá um erro
# Se você informar um diretório ao invés de um arquivo, teremos um IsADirectoryError

# Removendo diretórios

os.rmdir('temp2')

# Se o diretórios contiver qualquer conteudo teremos um OSError
# Se o diretório não exister teremos o erro FileNotFoundError

# Removendo todo o conteudo do diretorio]

for arquivo in os.scandir('temp2'):
    if arquivo.is_file():
        os.remove(arquivo.path)
    if not arquivo.is_file():
        os.rmdir(arquivo.path)

import tempfile

#criando diretorio temporario

with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei o diretório temporário em {tmp}')
    with open(os.path.join(tmp, 'teste.txt'), 'w') as arquivo:
        arquivo.write('Geek University')
    with open(os.path.join(tmp, 'teste.txt'), 'r') as arquivo:
        print(arquivo.read())
    input()

#criando arquivo temporario

with tempfile.TemporaryFile() as tmp:
    tmp.write(b'Geek University')
    tmp.seek(0)
    print(tmp.read())


"""

