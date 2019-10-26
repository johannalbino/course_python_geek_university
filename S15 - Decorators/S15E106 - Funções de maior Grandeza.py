"""
Funções de maior grandeza - Higber Order Functions (HOF)

O que isso significa?

- Quando uma linguagem de programação suportar HOF, indica que podemos ter funções que retornar outras funções como resultado ou mesmo que podemos passar funções como argumentos para
outras funções, e até mesmo criar variáveis do tipo de funções nos nossos programas.

OBS: Na seção de funções, nos utilizamos isso.

Em Python, as funções são Cidadões de Primeira Classe, First Class Citizen

# Exemplo - Definindo as funções


def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multi(a, b):
    return a * b


def dividir(a, b):
    return a / b


def calcular(num1, num2, funcao):
    return funcao(num1, num2)


#testando as funções

print(calcular(4, 3, somar))
print(calcular(4, 3, subtrair))
print(calcular(4, 3, multi))
print(calcular(4, 3, dividir))

# Nested Functions - Funções Aninhadas

# Em Python podemos também ter funções dentro de funções, que são conhecidas por Nested Functions
# ou também Inner Functions (Funções Internas)

# Exemplo

from random import choice


def cumprimento(pessoa):
    def humor():
        return choice(('E ai ', 'Suma daqui ', 'Gosto muito de você '))
    return humor() + pessoa

print(cumprimento('Johann'))
print(cumprimento('John'))

# Retornando funções de outras funções

from random import choice

def faz_me_rir():
    def rir():
        return choice(('hahahahahah', 'kkkkkkkkkk', 'yayayayayayayayay'))
    return  rir

rindo = faz_me_rir()

print(rindo())
"""

# Inner functions/Funções Internas/Nested Functions podem acessar o escopo de funções mais externas

from random import choice

def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(('hahahaha', 'lolololol', 'kkkkkkkkkk'))
        return f'{risada} {pessoa}'
    return dando_risada

rindo = faz_me_rir_novamente('Johann')

print(rindo())
