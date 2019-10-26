"""

Sistema de arquivos e navegação

Para fazer uso de manipulação de arquivos do sistema operacional, precisamos importar e fazer uso do módulo os.

os -> Operating System - Sistema Operacional

import os

# getcwd() -> pega o current work directory - diretório de trabalho corrente
# Retorna o path (caminho) absoluto
print(os.getcwd())

# Para mudar o diretório, podemos utilizar o chdir(path)
os.chdir('..')
print(os.getcwd())

#Podemos checar se o diretório é absoluto ou relativo
print(os.path.isabs(os.getcwd())) #Diretório absoluto
print(os.path.isabs('oi'))


# Podemos identificar o sistema operacional com o módulo os

print(os.name)
print(os.uname()) #Para linux


pasta_atual = os.getcwd()
os.chdir('..')
pasta_anterior = os.getcwd()

print(len(os.listdir(pasta_atual)) + len(os.listdir(pasta_anterior)))

"""

import os

# Podemos listar os arquivos e diretórios com mais detalhes com scandir()

arquivos = list(os.scandir())

print(arquivos)

print(dir(arquivos[0]))

print(arquivos[0].name) #nome do arquivo
print(arquivos[0].path) #caminho do arquivo
print(arquivos[0].inode())
print(arquivos[0].is_dir())
print(arquivos[0].stat())
