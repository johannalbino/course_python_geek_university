"""

Leitura de Arquivos

Para o conteúdo de um arquivo em Python, utilizamos a função integrada open()

open() -> Na forma mais simples de utilização nós passamos apenas um parâmetro de entrada, que neste caso é o nome/caminho do arquivo a ser lido. Essa função retorna um _io.TextIOWrapper e é com ele que trabalhamos então.

https://docs.python.org/3/library/functions.html#open

OBS: Por padrão, a função open abre o arquivo para leitura. Este arquivo deve existir, ou então teremos o erro FileNotFoundError

mode r -> Modo de leitura. r-> read() -> ler

"""

#Exemplo

arquivo = open('texto.txt')

print(arquivo)
print(type(arquivo))

# Para ler o conteúdo de um arquivo, após sua abertura, devemos utilizar a função read()

print(arquivo.read())

# OBS: O Python utiliza o recurso para trabalhar com arquivos chamado cursor, Esse cursor funciona como o cursor quando estamos escrevendo.
# A função read() lê todo o contéudo do arquivo.

print(arquivo.readline())
