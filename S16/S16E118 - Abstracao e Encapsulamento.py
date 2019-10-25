""""
Abstração e Encapsulamento


O grande objetivo da programação orientada a objeto é encapsular nosso código dentro de um grupo lógico e hierárquico
utilizando classes.

Encapsular -> Capsula
É o ato de encapsular os elementos de uma classe


             classe
-----------------------------------
|                                 |
|         atributos e métodos     |
-----------------------------------


Abstração, em POO, é o ato de expor apenas dados relevantes de uma classe, escondendo atributos e métodos privados de
usuário.

"""


class Conta:
    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com o limite de {self.__limite}')

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('O valor precisa ser positivo.')

    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
            else:
                print('Saldo insuficiente!')

        else:
            print('O valor deve ser positivo!')

    def transferir(self, valor, conta_destino):
        if valor > 0:
            # Remover o valor da conta de origem
            self.__saldo -= valor
            self.__saldo -= 10

            # Adicionar o valor na conta de destino
            conta_destino.__saldo += valor
        else:
            print('O valor precisa ser positivo.')


conta1 = Conta('Johann', 500.00, 1500)
conta2 = Conta('Ana', 200.00, 1200)

conta1.transferir(100, conta2)

conta1.extrato()
conta2.extrato()