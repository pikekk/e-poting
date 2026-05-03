import unittest
# Mengambil logika utama sistem dari folder app
from app.main_logic import SistemEVoting

class TestEVoting(unittest.TestCase):
    
    # ==========================================
    # INITIALIZATION (Persiapan Awal)
    # ==========================================
    
    @classmethod
    def setUpClass(cls):
        # Dipanggil sekali saat pengujian dimulai
        print("\n=== MENJALANKAN PENGUJIAN SISTEM E-VOTING ===")

    def setUp(self):
        # Dipanggil SETIAP KALI sebelum menjalankan satu fungsi test
        # Gunanya agar setiap test mendapatkan kondisi database yang bersih dan segar
        self.sistem = SistemEVoting()
        self.sistem.tambah_pemilih("P1", "User 1")
        self.sistem.tambah_kandidat("K1", "Calon A")

    # ==========================================
    # UNIT TESTING (Menguji Fungsi Spesifik)
    # ==========================================

    def test_voting_sukses(self):
        # Menguji apakah fungsi voting berjalan benar untuk pemilih & kandidat valid
        status, _ = self.sistem.voting("P1", "K1")
        
        # ASSERT: Memastikan status harus True. Jika False, test ini GAGAL.
        self.assertTrue(status)
        print("\nOutput: Unit Test Voting: PASS")

    def test_hitung_suara(self):
        # Menguji apakah penambahan angka suara pada kandidat sudah akurat (+1)
        self.sistem.voting("P1", "K1")
        
        # Mengakses jumlah suara langsung dari objek kandidat
        hasil = self.sistem.daftar_kandidat["K1"].jumlah_suara
        
        # ASSERT: Memastikan jumlah suara harus sama dengan 1
        self.assertEqual(hasil, 1)
        print("Output: Unit Test Hitung Suara: PASS")

    # ==========================================
    # INTEGRATION TESTING (Menguji Alur Sistem)
    # ==========================================

    def test_alur_lengkap(self):
        # Menguji gabungan beberapa aksi: tambah pemilih baru -> voting beruntun -> hasil akhir
        self.sistem.tambah_pemilih("P2", "User 2")
        self.sistem.voting("P1", "K1") # Suara pertama
        self.sistem.voting("P2", "K1") # Suara kedua
        
        hasil = self.sistem.daftar_kandidat["K1"].jumlah_suara
        
        # ASSERT: Memastikan integrasi dua suara masuk dengan benar ke kandidat yang sama
        self.assertEqual(hasil, 2)
        print("Output: Integration Test E-Voting: PASS")

    # ==========================================
    # FINALIZATION (Penutupan)
    # ==========================================

    @classmethod
    def tearDownClass(cls):
        # Dipanggil sekali setelah semua fungsi test selesai dijalankan
        print("\n=============================================")

if __name__ == '__main__':
    # Menjalankan seluruh rangkaian pengujian di atas
    unittest.main()