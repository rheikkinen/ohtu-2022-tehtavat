import statistics
import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(PlayerReaderStub())
    
    def test_etsitty_pelaaja_tulostetaan_oikein(self):
        etsitty_pelaaja = self.statistics.search("Kurri")
        self.assertAlmostEqual(str(etsitty_pelaaja), "Kurri EDM 37 + 53 = 90")

    def test_jos_pelaajaa_ei_ole_palautetaan_none(self):
        etsitty_pelaaja = self.statistics.search("Lehtinen")
        self.assertAlmostEqual(etsitty_pelaaja, None)

    def test_parhaat_pelaajat_listataan_oikeassa_jarjestyksessa(self):
        parhaat = self.statistics.top_scorers(4)
        oikea_jarjestys = [
            Player("Gretzky", "EDM", 35, 89),
            Player("Lemieux", "PIT", 45, 54),
            Player("Yzerman", "DET", 42, 56),
            Player("Kurri",   "EDM", 37, 53),
            Player("Semenko", "EDM", 4, 12)
        ]
        for pelaaja in parhaat:
            self.assertAlmostEqual(str(pelaaja), str(oikea_jarjestys[parhaat.index(pelaaja)]))

    def test_saman_joukkueen_pelaajat_haetaan_oikein(self):
        joukkue = self.statistics.team("EDM")
        oikea_lista = [
            Player("Semenko", "EDM", 4, 12),
            Player("Kurri",   "EDM", 37, 53),
            Player("Gretzky", "EDM", 35, 89)
        ]
        for pelaaja in joukkue:
            self.assertAlmostEqual(str(pelaaja), str(oikea_lista[joukkue.index(pelaaja)]))