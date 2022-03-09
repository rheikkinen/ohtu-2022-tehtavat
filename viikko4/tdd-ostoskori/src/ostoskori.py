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
        # lisää tuotteen ostoskoriin, jos sitä ei vielä ole korissa
        # kasvattaa tuotteen lukumäärää, jos tuote on jo korissa
        ostos = self.hae_ostos(lisattava)
        if ostos:
            ostos.muuta_lukumaaraa(1)
        else:
            self.ostoskori.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen, jos sitä on korissa vain yksi kpl
        # vähentää tuotteen lukumäärää, jos tuotetta on korissa useampi kpl
        ostos = self.hae_ostos(poistettava)
        if ostos:
            if ostos.lukumaara() == 1:
                del self.ostoskori[self.ostoskori.index(ostos)]
            else:
                ostos.muuta_lukumaaraa(-1)
                    
    def tyhjenna(self):
        # tyhjentää ostoskorin
        self.ostoskori.clear()

    def ostokset(self):
        # palauttaa listan jossa on korissa olevat Ostos-oliot
        # kukin Ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
        return self.ostoskori

    def hae_ostos(self, tuote: Tuote):
        # palauttaa Ostos-olion, jos se on korissa, muuten palauttaa None
        for ostos in self.ostoskori:
            if ostos.tuotteen_nimi() == tuote.nimi():
                return ostos
        return None