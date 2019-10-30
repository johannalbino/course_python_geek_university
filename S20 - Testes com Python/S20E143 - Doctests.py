"""
Doctests

São testes que colocamos na docstring das funções/méditos Python

Para executar doctests pelo terminal:

python -m doctest -v nome_do_modulo/arquivo.py

"""


def soma(a, b):
    """soma os números a e b

    >>> soma(1, 2)
    3
    """

    return a + b


#Outro exemplo aplicando o TDD


def duplicar_valores(valores):
    """duplica os valores em uma lista
     >>> duplicar_valores([1, 2, 3, 4])
     [2, 4, 6, 8]

     >>> duplicar_valores([])
     []

     >>> duplicar_valores(['a', 'b', 'c'])
     ['aa', 'bb', 'cc']

     >>> duplicar_valores([True, None])
     Traceback (most recent call last):
        ...
     TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """
    return [2 * elemento for elemento in valores]


def fala_oi():
    """Fala oi
    >>> fala_oi()
    'oi'
    """
    return "oi"

def retorna_verdade():
    """Retorna a verdade (True)
    >>> retorna_verdade()
    True
    """
    return True
