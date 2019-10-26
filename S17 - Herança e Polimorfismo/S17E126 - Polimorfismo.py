"""
Polimorfismo

Poli -> Muitas
Morfis -> Formas


Quando a gente reimplementa um método presente na classe pai em classes filhas estamos realizando uma sobrescrita de
método (Overriding)

O Overriding é a melhor representação do polimorfismo.

"""


class Animal(object):

    def __init__(self, nome):
        self.__nome = nome

    def falar(self):
        raise NotImplementedError('A classe filha precisa implementar este método!')

    def comer(self):
        print(f'{self.__nome} está comendo...')


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala auauauauau')


class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala miaumiaumiau')


class Rato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala algo....')


luck = Cachorro('Luck')
luck.comer()
luck.falar()

felix = Gato('Felix')
felix.falar()
felix.comer()

mickey = Rato('Mickey')
mickey.comer()
mickey.falar()
