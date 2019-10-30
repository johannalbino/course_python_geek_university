import unittest
from .robo import Robo


class RoboTest(unittest.TestCase):

	def setUp(self):
		self.megamen = Robo('Megaman', bateria=50)

	def test_carregar(self):
		self.megamen.carregar()
		self.assertEqual(self.megamen.bateria, 100)

	def test_dizer_nome(self):
		self.assertEqual(
			self.megamen.dizer_nome(),
			'BEEP BOOP BEEP BOOP. EU SOU MEGAMAN'
		)
		self.assertEqual(
			self.megamen.bateria, 49, 'A bateria deveria estar em 49%'
		)

	def tearDown(self):
		print('tearDown() sendo executado..')


if __name__ == '__main__':
	unittest.main()