from sovelluslogiikka import Sovelluslogiikka
from enum import Enum

class Komento(Enum):
    SUMMA = 1
    EROTUS = 2
    NOLLAUS = 3
    KUMOA = 4


class Komentotehdas:
    def __init__(self, io):
        self.io = io

        self.komennot = {
            Komento.SUMMA: Summa(self.io),
            Komento.EROTUS: Erotus(self.io),
            Komento.NOLLAUS: Nollaus(self.io),
            Komento.KUMOA: Kumoa(self.io)
        }
    
    def hae(self, komento):
        if komento in self.komennot:
            return self.komennot.get(komento)
        return None

class Summa:
    def __init__(self, sovelluslogiikka: Sovelluslogiikka):
        self.sovelluslogiikka = sovelluslogiikka

    def suorita(self, syote):
        arvo = 0
        try:
            arvo = int(syote)
        except Exception:
            pass

        self.sovelluslogiikka.plus(arvo)


class Erotus:
    def __init__(self, sovelluslogiikka: Sovelluslogiikka):
        self.sovelluslogiikka = sovelluslogiikka

    def suorita(self, syote):
        arvo = 0
        try:
            arvo = int(syote)
        except:
            pass

        self.sovelluslogiikka.miinus(arvo)

class Nollaus:
    def __init__(self, sovelluslogiikka: Sovelluslogiikka):
        self.sovelluslogiikka = sovelluslogiikka

    def suorita(self, syote):
        self.sovelluslogiikka.nollaa()

class Kumoa:
    def __init__(self, sovelluslogiikka: Sovelluslogiikka):
        self.sovelluslogiikka = sovelluslogiikka

    def suorita(self, syote):
        pass