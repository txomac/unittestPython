import datetime
import locale
import unittest

from OhceBuilder import OhceBuilder
from parameterized import parameterized

from src.PeriodeJournee import PeriodeDeLaJournee
from src.langue.Constantes import Constantes
from src.langue.LangueAng import LangueAnglaise
from src.langue.LangueFr import LangueFr
from LangueSpy import LangueSpy


class PalindromeTest(unittest.TestCase):

    @parameterized.expand([
        [LangueAnglaise(), Constantes.Anglais.WELL_DONE, Constantes.Anglais.GOOD_BYE]
    ])
    def test_palindrome(self, languechoisie, bien_dit, au_revoir):
        palindrome = "radar"

        ohce = OhceBuilder().langue(languechoisie).build()

        resultat = ohce.palindrome(palindrome)

        self.assertIn(palindrome + bien_dit + au_revoir, resultat)

    def test_non_palindrome(self):
        test = "thomas"
        palindrome = "radar"

        spy_langue = LangueSpy()
        ohce = OhceBuilder() \
            .langue(spy_langue) \
            .build()

        ohce.palindrome(test)

        self.assertEqual(0, spy_langue.nombre_appels_a_bien_dit)

    def test_saisie_client(self):
        locale_language, locale_encoding = locale.getlocale()
        current_time = datetime.datetime.now().time()
        chaine = input('Veuillez entrer une chaine à tester : ')

        if locale_language == 'fr_FR':
            langue_locale = LangueFr()
            if datetime.time(6) <= current_time < datetime.time(18):
                periode_locale = PeriodeDeLaJournee.MATIN
                bonjour_locale = Constantes.Francais.BONJOUR
            else:
                periode_locale = PeriodeDeLaJournee.NUIT
                bonjour_locale = Constantes.Francais.BONSOIR
            au_revoir_locale = Constantes.Francais.AU_REVOIR
            bien_dit_locale = Constantes.Francais.BIEN_DIT
        else:
            langue_locale = LangueAnglaise()
            if datetime.time(6) <= current_time < datetime.time(12):
                periode_locale = PeriodeDeLaJournee.MATIN
                bonjour_locale = Constantes.Anglais.GOOD_MORNING
            elif datetime.time(12) <= current_time < datetime.time(18):
                periode_locale = PeriodeDeLaJournee.APRES_MIDI
                bonjour_locale = Constantes.Anglais.GOOD_AFTERNOON
            elif datetime.time(18) <= current_time < datetime.time(22):
                periode_locale = PeriodeDeLaJournee.SOIR
                bonjour_locale = Constantes.Anglais.GOOD_EVENING
            else:
                periode_locale = PeriodeDeLaJournee.NUIT
                bonjour_locale = Constantes.Anglais.GOOD_NIGHT
            au_revoir_locale = Constantes.Anglais.GOOD_BYE
            bien_dit_locale = Constantes.Anglais.WELL_DONE

        ohcebuild = OhceBuilder().langue(langue_locale).periode(periode_locale).build()

        result = ohcebuild.palindrome(chaine)

        self.assertIn(bonjour_locale + chaine + bien_dit_locale + au_revoir_locale, result)


if __name__ == '__main__':
    unittest.main()
