"""
Preservando Metadata com Wraps

Metadatas -> São dados intrísecos em arquivos.

Wraps -> São funções que envolvem elementos com diversas finalidades.

#Problema

def ver_log(funcao):
    def logar(*args, **kwargs):
        Eu sou uma função (logar) dentro de outras
        print(f'Você está chamando: {funcao.__name__}')
        print(f'Aqui é documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar

@ver_log
def soma(a, b):
    Soma dois numeros
    return a + b


#print(soma(10, 30))
print(soma.__name__)  #Esta imprimindo o name da função do decorator
print(soma.__doc__) #Esta imprimindo o doc do decorator



"""

#Solucao

from functools import wraps


def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        """Eu sou uma função (logar) dentro de outras"""
        print(f'Você está chamando: {funcao.__name__}')
        print(f'Aqui é documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    """Soma dois numeros"""
    return a + b


print(soma(10, 30))
print(soma.__name__)
print(soma.__doc__)


