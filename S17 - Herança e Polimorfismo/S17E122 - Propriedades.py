"""
Propriedades

"""


class Conta:
    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    @saldo.setter
    def saldo(self, novo_saldo):
        self.__saldo = novo_saldo

    def extrato(self):
        return f'Saldo de {self.__saldo} do titular {self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, conta_destino):
        self.__saldo -= valor
        conta_destino.__saldo += valor

    @property
    def valor_total(self):
        return self.__saldo + self.__limite


conta1 = Conta('Johann', 3000, 5000)
conta2 = Conta('Herbert', 2000, 4000)

print(conta1.extrato())
print(conta2.extrato())

soma = conta1.saldo + conta2.saldo
print(f'A soma do saldo das contas é {soma}')


conta1.saldo = 7000

soma = conta1.saldo + conta2.saldo
print(f'A soma do saldo das contas é {soma}')
print(f'O saldo total (saldo + limite) do (a) {conta1.titular} é de {conta1.valor_total}')