# Introdução ao módulo Unittest

Unittest -> Testes Unitários

O que são testes unitários?

Teste é a forma de se testar unidades individuais de código Fonte.

Unidades individuais podem ser: funções, métodos, classes, módulos e etc...

OBS: Teste unitário não é especifico da linguagem Python.

Para criar nossos testes, criamos classes que herdam de unittest.TestCase e a partir de então ganhamos todos/todas
'assertions' presentes no módulo.

Para rodar os testes, utilizamos unittest.main()

TestCase -> Caso de teste para sua unidade

Asserts
https://docs.python.org/3/library/unittest.html

Por convenção, todos os testes em um test case devem ter seu nome iniciado com test_
Para executar os testes com unittest
python nome_do_modulo/arquivo.py

Para executar os testes com unittest no modo verbose
python nome_do_modulo/arquivo.py -v

Docstrings nos testes
Podemos acrescentar (e é recomendado) docstrings nos nossos testes
