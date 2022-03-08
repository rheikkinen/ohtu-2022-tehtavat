from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote
        self.ostoskori = []

    def tavaroita_korissa(self):
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 
        maara = 0
        for ostos in self.ostoskori:
            maara += ostos.lukumaara()
        
        return maara

    def hinta(self):
        # kertoo korissa olevien ostosten yhteenlasketun hinnan
        yhteensa = 0
        for ostos in self.ostoskori:
            yhteensa += ostos.hinta()

        return yhteensa

    def lisaa_tuote(self, lisattava: Tuote):
        tuotetta_ei_ole_korissa = True
        # tarkistetaan onko tuote jo ostoskorissa
        for ostos in self.ostoskori:
            # jos tuote on korissa, muutetaan sen lukumäärää
            if ostos.tuotteen_nimi() == lisattava.nimi():
                indeksi = self.ostoskori.index(ostos)
                self.ostoskori[indeksi].muuta_lukumaaraa(1)
                tuotetta_ei_ole_korissa = False
                break
        # jos tuotetta ei ole korissa, lisätään tuote koriin
        if tuotetta_ei_ole_korissa:
            self.ostoskori.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
        return self.ostoskori