import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()
        # luodaan kaksi tuotetta
        self.maito = Tuote("maito", 3)
        self.leipa = Tuote("leipä", 4)

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        self.kori.lisaa_tuote(self.maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korin_hinta_sama_kuin_tuotteen_hinta(self):
        self.kori.lisaa_tuote(self.maito)

        self.assertEqual(self.kori.hinta(), 3)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.leipa)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korin_hinta_sama_kuin_hintojen_summa(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.leipa)

        self.assertEqual(self.kori.hinta(), 7)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korin_hinta_2_kertaa_tuotteen_hinta(self):
        self.kori.lisaa_tuote(self.leipa)
        self.kori.lisaa_tuote(self.leipa)

        self.assertEqual(self.kori.hinta(), 8)

    def test_yhden_tuotteen_lisaamisen_korissa_yksi_ostos(self):
        self.kori.lisaa_tuote(self.maito)

        self.assertEqual(len(self.kori.ostokset()), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostos_jolla_oikea_nimi_ja_maara(self):
        self.kori.lisaa_tuote(self.maito)

        ostos = self.kori.ostokset()[0]
        # varmistetaan, että ostosolion nimi ja lukumäärä ovat oikeat
        self.assertEqual(ostos.tuotteen_nimi(), "maito")
        self.assertEqual(ostos.lukumaara(), 1)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_ostosta(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.leipa)
        # varmistetaan, että korissa on kaksi ostosta
        self.assertEqual(len(self.kori.ostokset()), 2)
        
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostos(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)
        # varmistetaan, että korissa on vain yksi Ostos-olio
        self.assertEqual(len(self.kori.ostokset()), 1)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostos_jolla_oikea_nimi_ja_lukumaara(self):
        # lisätään koriin kaksi samaa tuotetta
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)
        
        ostos = self.kori.ostokset()[0]
        # varmistetaan, että koriin lisätyllä ostoksella on oikea nimi ja lukumäärä
        self.assertEqual(ostos.tuotteen_nimi(), "maito")
        self.assertEqual(ostos.lukumaara(), 2)

    def test_jos_korissa_kaksi_samaa_tuotetta_ja_toinen_poistetaan_koriin_jaa_yksi_ostos_jonka_lukumaara_yksi(self):
        # lisätään koriin kaksi samaa tuotetta
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)
        # poistetaan toinen tuote korista
        self.kori.poista_tuote(self.maito)
        
        ostos = self.kori.ostokset()[0]
        # varmistetaan, että koriin lisätyn ostoksen lukumäärä on 1
        self.assertEqual(ostos.lukumaara(), 1)