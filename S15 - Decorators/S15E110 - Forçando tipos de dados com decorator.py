"""
Forçando tipo de dados com decorator



"""


def forca_tipo(*tipos):
    def decorador(funcao):
        def converte(*args, **kwargs):
            novo = []
            for (valor, tipo) in zip(args, tipos):
                novo.append(tipo(valor))
            return funcao(*novo, **kwargs)
        return converte
    return decorador


@forca_tipo(str, int)
def repete_msg(msg, vezes):
    for vez in range(vezes):
        print(f'{msg}')


print(repete_msg(1, 3))


@forca_tipo(float, float)
def dividir(a, b):
    return a/b


print(dividir('1', 5))