import unittest

from parameterized import parameterized

from OhceBuilder import OhceBuilder
from src.langue.Constantes import Constantes
from src.langue.LangueAng import LangueAnglaise
from src.langue.LangueFr import LangueFr


class SalutationTest(unittest.TestCase):

    @parameterized.expand(
        [
            [LangueAnglaise(), Constantes.Anglais.HELLO],
            [LangueFr(), Constantes.Francais.BONJOUR],
        ])
    def test_bonjour(self, languechoisie, attendu):
        ohce = OhceBuilder().langue(languechoisie).build()
        resultat = ohce.palindrome("test")

        self.assertEqual(attendu, resultat[0:len(attendu)])

    @parameterized.expand(
        [
            [LangueAnglaise(), Constantes.Anglais.GOOD_BYE],
            [LangueFr(), Constantes.Francais.AU_REVOIR],
        ])
    def test_au_revoir(self, languechoisie, attendu):
        ohce = OhceBuilder().langue(languechoisie).build()
        resultat = ohce.palindrome("test")

        self.assertEqual(attendu, resultat[-len(attendu):])
