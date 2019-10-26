""""
Atributos

Representam as características do objeto, ou seja, pelos atributos nós conseguimos representar computacionalmente os estados de um objeto.

Em Python, dividimos os atributos em 3 grupos:
    - Atributos de Instâncias;
    - Atributos de Classe;
    - Atributos Dinâmicos;

Atributo de instância:

São atributos declarados dentro do metodo construtor.
    - Metodo construtor é um metodo especial utilizado para a construção do objeto.

Em Python por convenção ficou estabelecido que todo atributo de uma classe é publico, ou seja, pode ser acessado em todo o projeto.
Caso queiramos demostrar que determinado atributo deve ser tratado como privado, ou seja, que deve ser acessado/utilizado somente dentro da própria classe onde está decladado,
utiliza-se __ duplo undercore no inicio de seu nome.

Isso também é conhecido como Name Mangling

class Lampada:

    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Produto:

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


#Atributos públicos ou/e privados


class Acesso:

    def __init__(self, email, senha):
        self.__email = email
        self.__senha = senha

    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.__email)

#OBS : Lembre-se que isso é apenas uma convenção, ou seja, a linguagem Python não vai impedir que façamos acesso aos atributos sinalizados como privados fora da classe.

#Exemplo:

user = Acesso('user@gmail.com', '123456')

print(user._Acesso__email)
print(user._Acesso__senha)   #AtributteError

print(dir(user))
user.mostra_senha()


# O que significa atributos de instância?

# Significa, que ao criarmos instâncias/objetos de uma classe, todas as intâncias terãos estes atributos

user1 = Acesso('user1@gmail.com', '123456')
user2 = Acesso('user2@gmail.com', '123789')

user1.mostra_email()
user2.mostra_email()




# Atributos de classe

p1 = Produto('PlayStation 4', 'Video Game', 2300)
p2 = Produto('Xbox S', 'Video Game', 4500)

# Atributos de classe, são atributos, claro que são declarados diretamente na classe, ou seja,
# fora do construtor. Geralmente já inicializamos um valor e este valor é compartilhado entre todas as instâncias da classe.
# Ou seja, ao invés de cada instância da classe ter seus próprios valores como é o caso dos atributos de instância, com os atributos
# de classe todas as instâncias terão o mesmo valor para este atributo


class Produto:

    # Atributo de classe
    imposto = 1.05  # 0.05% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id


pr1 = Produto('PlayStation 4', 'Video Game', 2300)
pr2 = Produto('Xbox S', 'Video Game', 4500)

print(pr1.valor) # Acesso possível, mas incorreto de um atributo de classe
print(pr2.valor) # Acesso possível, mas incorreto de um atributo de classe

print(Produto.imposto) # Acesso correto de um atributo de classe
print(Produto.contador)

"""

# Atributos dinamicos
# Um atributo de instância que pode ser criado em tempo de execução.
# OBS: O atributo dinamico será exclusivo da instância que o criou.


class Produto:

    # Atributo de classe
    imposto = 1.05  # 0.05% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id


p1 = Produto('PlayStation 4', 'Video Game', 2300)
p2 = Produto('Arroz', 'Mercearia', 5.99)

# Criando um atributo dinâmico em tempo de execução
p2.peso = '5 kg'  #Note que na classe produto não existe o atributo peso

print(f'Produto: {p2.nome}, Descricao: {p2.descricao}, Valor: {p2.valor}, Peso: {p2.peso}')
# print(f'Produto: {p1.nome}, Descricao: {p1.descricao}, Valor: {p1.valor}, Peso: {p1.peso}') #AttributeError

# Deletando atributos

print(p1.__dict__)
print(p2.__dict__)
print(Produto.__dict__)

del p2.peso

print(p1.__dict__)
print(p2.__dict__)
