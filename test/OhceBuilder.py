from src.Ohce import Ohce


class OhceBuilder:
    def __init__(self):
        self.__periode_journee = ""
        self.__langue = ""

    def build(self):
        return Ohce(self.__langue, self.__periode_journee)

    @staticmethod
    def default():
        return OhceBuilder().build()

    def langue(self, langue):
        self.__langue = langue
        return self

    def periode(self, periode_journee):
        self.__periode_journee = periode_journee
        return self
