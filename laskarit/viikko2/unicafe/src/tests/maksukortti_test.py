import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(10)
        self.assertEqual(str(self.maksukortti), "saldo: 0.2")

    def test_saldo_vahenee_oikein_jos_tarpeeksi_rahaa(self):
        self.maksukortti.ota_rahaa(3)
        self.assertEqual(str(self.maksukortti), "saldo: 0.07")
    
    def test_saldo_ei_muutu_jos_rahaa_ei_tarpeeksi(self):
        self.maksukortti.ota_rahaa(3)
        self.maksukortti.ota_rahaa(3)
        self.maksukortti.ota_rahaa(3)
        self.maksukortti.ota_rahaa(3)
        self.assertEqual(str(self.maksukortti), "saldo: 0.01")
    
    def test_metodi_palauttaa_true_jos_riittaa(self):
        self.maksukortti.ota_rahaa(9)
        self.assertTrue(str(self.maksukortti), True)
    def test_metodi_palauttaa_false_jos_ei_riitta(self):
        self.maksukortti.ota_rahaa(11)
        self.assertTrue(str(self.maksukortti), False)