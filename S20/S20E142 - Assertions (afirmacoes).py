"""
Assertions (Afirmações/Checagens/Questionamento)

Em Python utilizamos a palavra reservada 'assert' para realizar simples afirmações utilizadas nos testes

Utilizamos o 'assert' em uma expressão que queremos chegar se é válida ou não.

Se a expressão for verdadeira o 'assert' retorna None
Se for false levanta um erro do tipo AssertionError

OBS:
Nos podemos especificar opcionalmente um segundo argumento ou mesmo uma mensagem de erro personalizada
A palavra assert pode ser utilizada em qualquer função ou código nosso... não precisa ser exclusivamente nos testes

ALERTA - Cuidado ao utilizar o 'assert'

Se um programa Python for executado com o parâmetro -O, nenhum assertion será validado, ou seja, todas as validações
já eram.


def soma_numeros_positivos(a, b):
    assert a > 0 and b > 0, 'Ambos números precisam ser positivos'
    return a + b


ret = soma_numeros_positivos(2, 4) #6
print(ret)

ret1 = soma_numeros_positivos(-2, 4) #AssertionError
print(ret1)

"""

def comer_fast_food(comida):
    assert comida in [
        'pizza',
        'sorvete',
        'doces',
        'batatas fritas',
        'cachorro quente'
    ], 'A comida precisa ser Fast Food'

    return f'Eu estou comendo {comida}'


comer = comer_fast_food('pizza')
print(comer)

comer = comer_fast_food('morango')
print(comer)

