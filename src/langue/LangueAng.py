from src.langue.Constantes import Constantes
from src.PeriodeJournee import PeriodeDeLaJournee


class LangueAnglaise:

    def bonjour(self, periode_journee):
        match periode_journee:
            case PeriodeDeLaJournee.MATIN:
                return Constantes.Anglais.GOOD_MORNING
            case PeriodeDeLaJournee.APRES_MIDI:
                return Constantes.Anglais.GOOD_AFTERNOON
            case PeriodeDeLaJournee.SOIR:
                return Constantes.Anglais.GOOD_EVENING
            case PeriodeDeLaJournee.NUIT:
                return Constantes.Anglais.GOOD_NIGHT

        return Constantes.Anglais.HELLO

    def bien_dit(self):
        return Constantes.Anglais.WELL_DONE

    def au_revoir(self):
        return Constantes.Anglais.GOOD_BYE