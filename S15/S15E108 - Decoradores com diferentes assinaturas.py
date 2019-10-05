"""
Decorators com diferentes assinaturas

Assinatura de uma função é representada pelo seu retorno, nome e parâmetros de entrada

#Relembrando

def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá, eu sou o/a {nome}'

def ornerdar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal}, acompanhado de {acompanhamento} por favor!'

print(saudacao('Angelina'))

#Decorators Pattern


def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá, eu sou o/a {nome}'


@gritar
def orderdar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal}, acompanhado de {acompanhamento} por favor!'


print(saudacao('Angelina'))

print(orderdar('Picanha', 'Sorvete'))


@gritar
def lol():
    return 'lol'


print(lol())

#Vale lembrar que podemos utilizar parametro nomeados


print(orderdar(acompanhamento='Batata Frita', principal='Picanha'))

"""

# Decorator com argumentos

def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto! Primeiro argumento precisa ser {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna


@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    print(args)

@verifica_primeiro_argumento(10)
def soma_dez(num1, num2):
    return num1 + num2


print(soma_dez(10, 12))
print(soma_dez(1, 21))


print(comida_favorita('pizza', 'churrasco'))
print(comida_favorita('churrasco', 'pizza'))