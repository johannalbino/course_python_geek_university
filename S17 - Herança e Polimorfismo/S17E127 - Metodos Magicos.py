"""
Metodos Magicos

São todos os métodos que utilizam dunder

dunder init -> __init__

Dunder -> Double Underscore


"""


class Livro:

    def __init__(self, titulo, autor, paginas):
        self.__titulo = titulo
        self.__autor = autor
        self.__paginas = paginas

    def __repr__(self):
        return f'{self.__titulo} escrito por {self.__autor}'

    def __str__(self):
        return self.__titulo

    def __len__(self):
        return self.__paginas

    def __add__(self, other):
        return f'{self} - {other}'

    def __mul__(self, other):
        if isinstance(other, int):
            msg = ''
            for n in range(other):
                msg += ' ' + str(self)
            return msg
        return 'Não posso multiplicar.'

    def __del__(self):
        return 'Você deletou o livro!'


livro1 = Livro('Python Rocks!', 'Geek University', 400)
livro2 = Livro('Inteligência Artificial com Python', 'Geek University', 350)


print(livro1.__repr__())
print(livro2)
print(livro2.__len__())
print(livro1 + livro2)
print(livro1 * 3)
