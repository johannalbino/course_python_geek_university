"""
Alocação e Gerência de Memória em Python

quando um objeto não tem mais referencia, vira um DeadObject na memoria, um objeto sem referencia

O algoritmo utilizado pelo Garbage Collector do Python é chamado de Reference Counting

Diferentes linguagens de programação utilizam diferentes algoritmos para o Garbage Collector

Ate mesmo diferentes implementações da linguagem Python utilizam diferentes implementações para o Garbage
Collector: CPython, PyPy, IronPython, Stackless, Jython

Métodos e variáveis são criadas na memória Stack
Os objetos e instancias são criadas na memória heap
Um novo stack é criado durante a invocação de uma função ou método
Stacks são destruidas sempre que uma função ou método retorna valor.
Garbage Collector é um mecanismo para limpar dead objects

"""

x = 10
print(type(x))
y = x
y += 1
if id(y) == id(x):
	print('Y e X alocam a mesma memória')
else:
	print('Não alocam a mesma memória')