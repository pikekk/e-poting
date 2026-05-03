import unittest
from app.main_logic import SistemEVoting

class TestEVoting(unittest.TestCase):
    def setUp(self):
        self.sistem = SistemEVoting()
        self.sistem.tambah_pemilih("P1", "User 1")
        self.sistem.tambah_kandidat("K1", "Calon A")

    # UNIT TEST
    def test_voting_sukses(self):
        status, _ = self.sistem.voting("P1", "K1")
        self.assertTrue(status)

    def test_mencegah_duplikasi(self):
        self.sistem.voting("P1", "K1")
        status_kedua, _ = self.sistem.voting("P1", "K1")
        self.assertFalse(status_kedua)

    # INTEGRATION TEST
    def test_alur_lengkap(self):
        self.sistem.tambah_pemilih("P2", "User 2")
        self.sistem.voting("P1", "K1")
        self.sistem.voting("P2", "K1")
        hasil = self.sistem.daftar_kandidat["K1"].jumlah_suara
        self.assertEqual(hasil, 2)

if __name__ == '__main__':
    unittest.main()