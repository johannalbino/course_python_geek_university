import unittest
from .atividades import comer, dormir, engracado


class AtividadesTest(unittest.TestCase):
    def test_comer(self):
        """Testando o retorno com comida saudavel"""
        self.assertEqual(
            comer('quiabo', True),
            'Estou comendo quiabo porque quero manter a forma.'
        )

    def test_comer_gostosa(self):
        """Testando o retorno com comida gostosa"""
        self.assertEqual(
            comer(comida='pizza', saudavel=False),
            'Estou comendo pizza porque a gente só vive uma vez.'
        )

    def test_dormir_pouco(self):
        """Testando o retorno com dormindo pouco"""
        self.assertEqual(
            dormir(4),
            'Continuo cansado após dormir por 4 horas. :('
        )

    def test_dormir_muito(self):
        """Testando o retorno dormindo muito"""
        self.assertEqual(
            dormir(10),
            'Putz! Dormir muito! Estou atrasado para o trabalho!'
        )

    def test_engracado(self):
        """Testando se e engracado"""
        #self.assertEqual(engracado('Sérgio Malandro'), False)
        self.assertFalse(engracado('Sérgio Malandro'))
        self.assertTrue(engracado('Jim Carrey'), 'Jim Carrey deveria ser engraçado.')


if __name__ == '__main__':
    unittest.main()
