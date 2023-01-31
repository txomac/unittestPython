import unittest

from parameterized import parameterized

from OhceBuilder import OhceBuilder
from src.PeriodeJournee import PeriodeDeLaJournee
from src.langue.Constantes import Constantes
from src.langue.LangueAng import LangueAnglaise
from src.langue.LangueFr import LangueFr


class SalutationTest(unittest.TestCase):

    @parameterized.expand(
        [
            [LangueAnglaise(), PeriodeDeLaJournee.DEFAULT, Constantes.Anglais.HELLO],
            [LangueAnglaise(), PeriodeDeLaJournee.MATIN, Constantes.Anglais.GOOD_MORNING],
            [LangueAnglaise(), PeriodeDeLaJournee.APRES_MIDI, Constantes.Anglais.GOOD_AFTERNOON],
            [LangueAnglaise(), PeriodeDeLaJournee.SOIR, Constantes.Anglais.GOOD_EVENING],
            [LangueAnglaise(), PeriodeDeLaJournee.NUIT, Constantes.Anglais.GOOD_NIGHT],
            [LangueFr(), PeriodeDeLaJournee.DEFAULT, Constantes.Francais.BONJOUR],
            [LangueFr(), PeriodeDeLaJournee.MATIN, Constantes.Francais.BONJOUR],
            [LangueFr(), PeriodeDeLaJournee.APRES_MIDI, Constantes.Francais.BONJOUR],
            [LangueFr(), PeriodeDeLaJournee.SOIR, Constantes.Francais.BONSOIR],
            [LangueFr(), PeriodeDeLaJournee.NUIT, Constantes.Francais.BONSOIR],
        ])
    def test_bonjour(self, languechoisie, periodechoisie, attendu):
        ohce = OhceBuilder().langue(languechoisie).periode(periodechoisie).build()
        resultat = ohce.palindrome("test")

        self.assertEqual(attendu, resultat[0:len(attendu)])

    @parameterized.expand(
        [
            [LangueAnglaise(), PeriodeDeLaJournee.DEFAULT, Constantes.Anglais.GOOD_BYE],
            [LangueFr(), PeriodeDeLaJournee.DEFAULT, Constantes.Francais.AU_REVOIR],
        ])
    def test_au_revoir(self, languechoisie, periodechoisie, attendu):
        ohce = OhceBuilder().langue(languechoisie).periode(periodechoisie).build()
        resultat = ohce.palindrome("test")

        self.assertEqual(attendu, resultat[-len(attendu):])
