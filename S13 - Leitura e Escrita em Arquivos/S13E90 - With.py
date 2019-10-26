"""
Bloco with

O bloco with é utilizado para criar um contexto de trabalho onde os recursos utilizados são fechados após o bloco with.

"""

with open('texto.txt') as arquivo:
    print(arquivo.readlines())