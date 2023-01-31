from src.langue.Constantes import Constantes
from src.PeriodeJournee import PeriodeDeLaJournee


class LangueFr:

    def bonjour(self, periode_journee):
        return Constantes.Francais.BONSOIR \
            if periode_journee in (PeriodeDeLaJournee.SOIR, PeriodeDeLaJournee.NUIT)\
            else Constantes.Francais.BONJOUR

    def bien_dit(self):
        return Constantes.Francais.BIEN_DIT

    def au_revoir(self):
        return Constantes.Francais.AU_REVOIR