"""
Herança Multipla

A Herança Múltipla nada mais é do que a possibilidade de uma classe herdar de múltiplas classes,
fazendo com que a classe filha herde todos os atributos e métodos de todas as classes herdadas

Observação: A Herança múltipla pode ser feita de duas maneiras:
    - Por Multiderivação Direta;
    - Por Multiderivação Indireta.


#Exemplo 1 - Multiderivação Direta


class Base1:
    pass


class Base2:
    pass


class MultiDerivada(Base1, Base2):
    pass


#Exemplo 2 - Multiderivação Indireta


class Base1:
    pass


class Base2(Base1):
    pass


class MultiDerivada(Base2):
    pass

Não importa se a derivação é direta ou indireta. A classe que realizar a herança herdará todos os atributos e métodos
das super classes.

"""


class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f'Eu sou {self.__nome}'


class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} está nadando.'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} do mar'


class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} está andando.'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} da terra.'


class Pinguim(Terrestre, Aquatico):

    def __init__(self, nome):
        super().__init__(nome)


baleia = Aquatico('Wally')
print(baleia.nadar())
print(baleia.cumprimentar())

tatu = Terrestre('Xim')
print(tatu.andar())
print(tatu.cumprimentar())

pinguim = Pinguim('Tux')
print(pinguim.andar())
print(pinguim.nadar())
print(pinguim.cumprimentar())


print(f'Tux é instância de Pinguim? {isinstance(pinguim, Pinguim)}')
print(f'Tux é instância de Aquatico? {isinstance(pinguim, Aquatico)}')
print(f'Tux é instância de Terrestre? {isinstance(pinguim, Terrestre)}')
print(f'Tux é instância de object? {isinstance(pinguim, object)}')
