"""
Seek e Cursors

seek() -> É utilizado para movimentar o cursor pelo arquivo.

arquivo = open('texto.txt')

print(arquivo.read())

# A função seek é utilizada para movimentação do cursor pelo arquivo. Ela recebe um parâmetro que indica onde queremos colocar o cursor
# Movimentando o cursor pelo arquivo com a função seek()

#Voltando para a posição 0 do texto, colocando o curso na posição 0
arquivo.seek(0)

print(arquivo.read())

# readline() -> Função que lê o arquivo linha a linha.

print(arquivo.readline())
print(arquivo.readline())


# readlines()

linhas = arquivo.readlines()

print(linhas)
print(type(linhas))
print(linhas.__len__())

"""

#OBS: Quando abrimos um arquivo com a função open() é criada uma conexão entre o arquivo no disco do computador e o programa Python. Essa conexão é chamada de streaming.
# Ao finalizar os trabalhos com o arquivo devemos fechar essa conexão. Para isso utilizamso a função clone()

arquivo = open('texto.txt')

print(arquivo.read())

print(arquivo.closed) #Verifica se o arquivo está aberto ou fechado - True: Arquivo fechado / False: Arquivo aberto

arquivo.close()

print(arquivo.closed)