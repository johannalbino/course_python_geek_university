"""
Unittest - Antes e após hooks

hooks - São os testes em si, ou seja, a execução dos testes

setUp() - É executado antes de cada método de teste. É util para criarmos instâncias de objetos e outros dados.

tearDown() - É executado ao final de cada método de teste. É útil para excluir dados ou fechar conexões com banco de
dados.
"""
import unittest


class ModuloTest(unittest.TestCase):

	def setUp(self):
		pass

	def test_primeiro(self):
		pass

	def tearDown(self):
		pass