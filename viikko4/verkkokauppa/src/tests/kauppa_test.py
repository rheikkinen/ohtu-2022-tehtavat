import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock(wraps=Viitegeneraattori())
        self.varasto_mock = Mock()

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            
            if tuote_id == 2:
                return 5

            if tuote_id == 3:
                return 0

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            
            if tuote_id == 2:
                return Tuote(2, "leipä", 6)

            if tuote_id == 3:
                return Tuote(3, "jogurtti", 4)

        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)


    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        # palautetaan aina arvo 42
        self.viitegeneraattori_mock.uusi.return_value = 42

        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_arvoilla(self):
        # palautetaan aina arvo 42
        self.viitegeneraattori_mock.uusi.return_value = 42

        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikeilla parametreilla
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 5)

    def test_kahta_eri_tuotetta_ostettaessa_metodia_tilisiirto_kutsutaan_oikeilla_arvoilla(self):
        # palautetaan aina arvo 42
        self.viitegeneraattori_mock.uusi.return_value = 42
        
        # ostetaan kaksi eri tuotetta
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("leena", "54321")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikeilla parametreilla
        self.pankki_mock.tilisiirto.assert_called_with("leena", 42, "54321", "33333-44455", 11)

    def test_kahta_samaa_tuotetta_ostettaessa_metodia_tilisiirto_kutsutaan_oikeilla_arvoilla(self):
        # palautetaan aina arvo 42
        self.viitegeneraattori_mock.uusi.return_value = 42
        
        # ostetaan samaa tuotetta kaksi kappaletta
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("leena", "54321")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikeilla parametreilla
        self.pankki_mock.tilisiirto.assert_called_with("leena", 42, "54321", "33333-44455", 12)

    def test_tuotetta_jota_ei_ole_varastossa_ei_lasketa_mukaan_ostoksiin(self):
        # palautetaan aina arvo 42
        self.viitegeneraattori_mock.uusi.return_value = 42
        
        # ostetaan varastossa oleva tuote ja tuote, jota ei ole varastossa
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("kalle", "11111")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikeilla parametreilla
        self.pankki_mock.tilisiirto.assert_called_with("kalle", 42, "11111", "33333-44455", 5)

    def test_uuden_asioinnin_aloittaminen_nollaa_edelliset_ostokset(self):
        # palautetaan aina arvo 42
        self.viitegeneraattori_mock.uusi.return_value = 42
        
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2) # hinta 6
        self.kauppa.tilimaksu("leena", "54321")
        
        # aloitetaan uusi asiointi
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1) # hinta 5
        self.kauppa.tilimaksu("leena", "54321")

        # varmistetaan että aiempia ostoksia ei laskettu mukaan uusien ostosten loppusummaan
        self.pankki_mock.tilisiirto.assert_called_with("leena", 42, "54321", "33333-44455", 5)

    def test_jokaiselle_maksutapahtumalle_annetaan_uusi_viitenumero(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("leena", "54321")

        # varmistetaan, että kaupan antama viitenumero oli 2
        self.pankki_mock.tilisiirto.assert_called_with(ANY, 2, ANY, ANY, ANY)
        
        # suoritetaan uusi asiointi
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("leena", "54321")
        
        # varmistetaan, että kaupan antama viitenumero nyt oli 3
        self.pankki_mock.tilisiirto.assert_called_with(ANY, 3, ANY, ANY, ANY)

    def test_ostoskorista_poistettua_tuotetta_ei_lasketa_ostosten_loppusummaan(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2) # hinta 6
        self.kauppa.lisaa_koriin(1) # hinta 5
        self.kauppa.poista_korista(2)
        self.kauppa.tilimaksu("leena", "54321")

        # varmistetaan, että ostoskorista poistettu tuote ei näy loppusummassa
        self.pankki_mock.tilisiirto.assert_called_with(ANY, ANY, ANY, ANY, 5)
