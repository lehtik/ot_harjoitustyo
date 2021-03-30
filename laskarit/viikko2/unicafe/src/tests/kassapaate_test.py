import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassipaate = Kassapaate()
        self.pankkikortti = Maksukortti(1000)
        self.kassipaate.kassassa_rahaa = 1000
        self.kassipaate.edulliset = 0
        self.kassipaate.maukkaat = 0

    def test_rahamaara_oikea(self):
        self.assertEqual(self.kassipaate.kassassa_rahaa, 1000)
        self.assertEqual(self.kassipaate.edulliset, 0)
        self.assertEqual(self.kassipaate.maukkaat, 0)

    def test_ei_myytyja_lounaita(self):
        self.assertEqual(self.kassipaate.edulliset, 0)
        self.assertEqual(self.kassipaate.maukkaat, 0)

    def test_maksu_riittava_kassan_rahamaara_kasvaa_vaihtoraha_on_oikea(self):
        self.kassipaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassipaate.kassassa_rahaa, 1240)
        self.assertTrue(self.kassipaate, True)
    
    def test_riittavaa_maksu_edullisten_maara(self):
        self.kassipaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassipaate.edulliset, 1)
        self.assertTrue(self.kassipaate, True)

    def test_maksu_riittava_maukkaasti_kassan_rahamaara_kasvaa_vaihtoraha_on_oikea(self):
        self.kassipaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassipaate.kassassa_rahaa, 1400)
        self.assertTrue(self.kassipaate, True)

    def test_riittavaa_maksu_maukkaiden_maara(self):
        self.kassipaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassipaate.maukkaat, 1)
        self.assertTrue(self.kassipaate, True)

    def test_maksu_ei_edukkaasti_riittava_kateinen(self):
        self.kassipaate.syo_edullisesti_kateisella(230)
        self.assertEqual(self.kassipaate.kassassa_rahaa, 1000)
        self.assertEqual(self.kassipaate.edulliset, 0)
        self.assertTrue(self.kassipaate, False)

    def test_maksu_ei_maukkaasti_riittava_kateinen(self):
        self.kassipaate.syo_maukkaasti_kateisella(390)
        self.assertEqual(self.kassipaate.kassassa_rahaa, 1000)
        self.assertEqual(self.kassipaate.maukkaat, 0)
        self.assertTrue(self.kassipaate, False)

    def test_kortilla_rahaa_edullisesti_summa_veloitettu_arvo_true(self):
        self.kassipaate.syo_edullisesti_kortilla(self.pankkikortti)
        self.kassipaate.syo_edullisesti_kortilla(self.pankkikortti)
        self.kassipaate.syo_edullisesti_kortilla(self.pankkikortti)
        self.kassipaate.syo_edullisesti_kortilla(self.pankkikortti)
        self.assertTrue(self.kassipaate, True)
        self.assertEqual(self.kassipaate.edulliset, 4)
        self.assertEqual(self.pankkikortti.saldo, 40)
        self.assertEqual(self.kassipaate.kassassa_rahaa, 1000)

    def test_kortilla_rahaa_maukkaasti_summa_veloitettu_arvo_true(self):
        self.kassipaate.syo_maukkaasti_kortilla(self.pankkikortti)
        self.kassipaate.syo_maukkaasti_kortilla(self.pankkikortti)
        self.assertTrue(self.kassipaate, True)
        self.assertEqual(self.kassipaate.maukkaat, 2)
        self.assertEqual(self.pankkikortti.saldo, 200)
        self.assertEqual(self.kassipaate.kassassa_rahaa, 1000)

    def test_kortilla_ei_rahaa_summa_ei_veloitettu_arvo_false(self):
        self.kassipaate.syo_maukkaasti_kortilla(self.pankkikortti)
        self.kassipaate.syo_maukkaasti_kortilla(self.pankkikortti)
        self.kassipaate.syo_maukkaasti_kortilla(self.pankkikortti)
        self.assertTrue(self.kassipaate, False)
        self.assertEqual(self.pankkikortti.saldo, 200)
        self.assertEqual(self.kassipaate.kassassa_rahaa, 1000)

    def test_kortilla_ei_edullisesti_rahaa_summa_ei_veloitettu_arvo_false(self):
        self.kassipaate.syo_edullisesti_kortilla(self.pankkikortti)
        self.kassipaate.syo_edullisesti_kortilla(self.pankkikortti)
        self.kassipaate.syo_edullisesti_kortilla(self.pankkikortti)
        self.kassipaate.syo_edullisesti_kortilla(self.pankkikortti)
        self.kassipaate.syo_edullisesti_kortilla(self.pankkikortti)
        self.assertTrue(self.kassipaate, False)
        self.assertEqual(self.pankkikortti.saldo, 40)
        self.assertEqual(self.kassipaate.kassassa_rahaa, 1000)

    def test_kortille_rahaa_saldo_muuttuu_kassaraha_kasvaa(self):
        self.kassipaate.lataa_rahaa_kortille(self.pankkikortti, 400)
        self.assertEqual(self.pankkikortti.saldo, 1400)
        self.assertEqual(self.kassipaate.kassassa_rahaa, 1400)

    def test_kortille_negarahaa_saldo_muuttuu_kassaraha_kasvaa(self):
        self.kassipaate.lataa_rahaa_kortille(self.pankkikortti, -400)
        self.assertEqual(self.pankkikortti.saldo, 1000)
        self.assertEqual(self.kassipaate.kassassa_rahaa, 1000)

    def test_pankkikortille_rahaa_saldo_muuttuu(self):
        self.pankkikortti.lataa_rahaa(400)
        self.pankkikortti.ota_rahaa(200)
        self.assertEqual(self.pankkikortti.saldo, 1200)
        self.assertEqual(self.kassipaate.kassassa_rahaa, 1000)

