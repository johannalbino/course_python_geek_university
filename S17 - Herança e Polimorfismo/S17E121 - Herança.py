""""
Herança (Inheritance)

A ideia de herança é a de reaproveitar código, também estender nossas classes.

Com herança a partir de uma classe existente, nós extendemos outra classe que passa a herdar atributos e métodos da
classe herdada.


Cliente:
    - nome
    - sobrenome
    - cpf
    - renda

Funcionário:
    - nome
    - sobrenome
    - cpf
    - matricula

Quando uma classe herda de outra classe, ela herda TODOS os atributos e métodos da classe herdada.

Qaundo uma classe herda de outra classe, a classe herdadada é conhecida por:
    - Super Classe
    - Classe Mãe
    - Classe Pai
    - Classe Base
    - Classe Genérica

Quando uma classe herda de outra classe, ela é chamada:
    - Sub Classe
    - Classe Filha
    - Classe Específica


"""


class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    """Cliente herda de Pessoa"""
    def __init__(self, nome, sobrenome, cpf, renda):
        Pessoa.__init__(self, nome, sobrenome, cpf)   # Forma não comum de acessar dados da super classe
        self.__renda = renda


class Funcionario(Pessoa):
    """Cliente herda de Pessoa"""
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)    # Forma comum de acessar dados da super classe
        self.__matricula = matricula

    def nome_completo(self):
        print(super().nome_completo())
        print(self._Pessoa__cpf)
        return f'Funcionario: {self.__matricula} Nome: {self._Pessoa__nome}'

# Sobrescrita de Métodos (Overriding)
# Ocorre quando reescrevemos um metodo presente na super classe em uma classe/classes filhas


cliente1 = Cliente('Johann', 'Herbert', '123456789', 20000.00)
funcionario1 = Funcionario('Albino', 'Jeronimo', '123456789', 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())

print(cliente1.__dict__)
print(funcionario1.__dict__)

