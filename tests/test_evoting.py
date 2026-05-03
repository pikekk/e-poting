import unittest
from app.main_logic import SistemEVoting

class TestEVoting(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("\n=== MENJALANKAN PENGUJIAN SISTEM E-VOTING ===")

    def setUp(self):
        self.sistem = SistemEVoting()
        self.sistem.tambah_pemilih("P1", "User 1")
        self.sistem.tambah_kandidat("K1", "Calon A")

    def test_voting_sukses(self):
        status, _ = self.sistem.voting("P1", "K1")
        self.assertTrue(status)
        print("\nOutput: Unit Test Voting: PASS")

    def test_hitung_suara(self):
        self.sistem.voting("P1", "K1")
        hasil = self.sistem.daftar_kandidat["K1"].jumlah_suara
        self.assertEqual(hasil, 1)
        print("Output: Unit Test Hitung Suara: PASS")

    def test_alur_lengkap(self):
        self.sistem.tambah_pemilih("P2", "User 2")
        self.sistem.voting("P1", "K1")
        self.sistem.voting("P2", "K1")
        hasil = self.sistem.daftar_kandidat["K1"].jumlah_suara
        self.assertEqual(hasil, 2)
        print("Output: Integration Test E-Voting: PASS")

    @classmethod
    def tearDownClass(cls):
        print("\n=============================================")

if __name__ == '__main__':
    unittest.main()