"""
Metodos

- Metodos (funções) - Representam os comportamentos do objeto, ou seja, as ações que este objeto pode realizar no seu sistema.

Em Python, dividimos os métodos em 2 grupos:
- Métodos de instância
- Métodos de classe


#Metodos de Instância

O metodo de dunder __init__ é um metodo especial chamado de construtor e sua função é construir o objeto a partir da classe

OBS: Todo elemento em Python que inicia e finaliza com duplo underline é chamado de dunder

"""

class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade


class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """
        Retorna o valor do produto com o desconto
        :param porcentagem:
        :return:
        """
        return (self.__valor * (100 - porcentagem)) / 100


from passlib.hash import pbkdf2_sha256 as cryp


class Usuario:

    contador = 0

    @classmethod
    def conta_usuarios(cls):
        print(f'Temos {cls.contador} usuários no sistema')

    def __init__(self, nome, sobrenome,  email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=20000, salt_size=16)
        Usuario.contador = self.__id
        print(f'Usuario criado: {self.__gera_usuario()}')

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

    def __gera_usuario(self):
        return self.__email.split('@')[0]

    @staticmethod
    def definicao():
        return 'UXR344'


p1 = Produto('Playstation 4', 'Video Game', 2300)
print(f'O valor do produto com 10% de desconto é de: R${p1.desconto(10)}')
print(f'O valor do produto com 20% de desconto é de: R${p1.desconto(20)}')
print(f'O valor do produto com 50% de desconto é de: R${p1.desconto(50)}')

u1 = Usuario('Johann', 'Albino', 'johann.albino@gmail.com', '123456')


print('================')
nome = 'Johann' #input('Informe o nome: ')
sobrenome = 'Albino' #input('Informe o sobrenome: ')
email = 'johann@gmail.com' #input('Informe o email: ')
senha = '123456' #input('Informe a senha: ')
confirme_senha = '123456' #input('Confirme a senha: ')

if senha == confirme_senha:
    user = Usuario(nome, sobrenome, email, senha)
    print('Usuário criado com sucesso!')
else:
    print('Senha não confere...')
    print('Usuário não foi criado!')
    exit()

senha = '123456' #input('Informe a senha para acesso: ')

if user.checa_senha(senha):
    print('Acesso permitido')

else:
    print('Acesso negado.')

print(f'Senha User Criptografada: {user._Usuario__senha}')


"""
Metodos de classe

Para utilizar o metodo de classe é necessario utilizar o decorator @classmethod
São conhecido como metodos estaticos em outras linguagens

"""

print(Usuario.conta_usuarios())

"""
Metodos Estaticos

Os metodos estaticos são parecidos com o de classe, mas utiliza o decorador @staticmethod

"""

print(Usuario.definicao())