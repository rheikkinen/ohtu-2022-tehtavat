KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko

        self.lukujono = [0] * self.kapasiteetti

        self.alkioiden_lkm = 0

    def kuuluu_joukkoon(self, n):
        for luku in self.lukujono:
            if n == luku:
                return True
        return False

    def lisaa(self, lisattava):
        if not self.kuuluu_joukkoon(lisattava):
            self.lukujono[self.alkioiden_lkm] = lisattava
            self.alkioiden_lkm += 1

            if self.alkioiden_lkm % len(self.lukujono) == 0:
                self.lukujono += [0] * self.kasvatuskoko

            return True

        return False

    def poista(self, poistettava):
        if self.kuuluu_joukkoon(poistettava):
            kohta = self.lukujono.index(poistettava)
            self.lukujono[kohta] = 0

            for j in range(kohta, self.alkioiden_lkm - 1):
                self.lukujono[j] = self.lukujono[j + 1]

            self.alkioiden_lkm -= 1
            return True

        return False

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = [0] * self.alkioiden_lkm

        for i in range(0, len(taulu)):
            taulu[i] = self.lukujono[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.lukujono[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos += str(self.lukujono[i])
                tuotos += ", "
            tuotos += str(self.lukujono[self.alkioiden_lkm - 1])
            tuotos += "}"
            return tuotos
