# ==========================================
# ENTITAS 1: PEMILIH
# ==========================================
class Pemilih:
    def __init__(self, id_pemilih, nama):
        # Menyimpan ID unik pemilih (seperti NIK atau NIM)
        self.id_pemilih = id_pemilih 
        # Menyimpan nama lengkap pemilih
        self.nama = nama 
        # FLAG KRUSIAL: Status awal selalu False (belum mencoblos)
        # Ini digunakan untuk mencegah pemilih memberikan suara lebih dari satu kali
        self.sudah_memilih = False 

# ==========================================
# ENTITAS 2: KANDIDAT
# ==========================================
class Kandidat:
    def __init__(self, id_kandidat, nama):
        # ID unik untuk mengenali kandidat (misal: nomor urut 01)
        self.id_kandidat = id_kandidat 
        # Nama calon yang akan dipilih
        self.nama = nama 
        # Counter untuk menampung total perolehan suara
        self.jumlah_suara = 0 

# ==========================================
# SISTEM UTAMA (BRAIN)
# ==========================================
class SistemEVoting:
    def __init__(self):
        # Menggunakan Dictionary (Kamus) agar pencarian ID sangat cepat
        # Formatnya -> { "ID_KANDIDAT": Objek_Kandidat }
        self.daftar_pemilih = {}
        self.daftar_kandidat = {}

    def tambah_pemilih(self, id_pemilih, nama):
        # Membuat objek Pemilih baru dan menyimpannya ke database (Dictionary)
        self.daftar_pemilih[id_pemilih] = Pemilih(id_pemilih, nama)

    def tambah_kandidat(self, id_kandidat, nama):
        # Membuat objek Kandidat baru dan menyimpannya ke database (Dictionary)
        self.daftar_kandidat[id_kandidat] = Kandidat(id_kandidat, nama)

    def voting(self, id_pemilih, id_kandidat):
        """
        Fungsi ini adalah inti dari sistem pengujian (Main Logic).
        Output berupa: (Status_Boolean, Pesan_String)
        """
        
        # VALIDASI 1: Cek apakah ID pemilih ada dalam database
        if id_pemilih not in self.daftar_pemilih:
            return False, "ID Tidak Terdaftar"
        
        # Mengambil data objek pemilih dari dictionary
        pemilih = self.daftar_pemilih[id_pemilih]
        
        # VALIDASI 2: Cek apakah pemilih sudah pernah memilih sebelumnya
        # Jika status 'sudah_memilih' sudah True, maka akses ditolak
        if pemilih.sudah_memilih:
            return False, "Sudah Memilih"
        
        # VALIDASI 3: Cek apakah ID kandidat yang dipilih ada dalam list
        if id_kandidat not in self.daftar_kandidat:
            return False, "Kandidat Tidak Ada"
        
        # --- PROSES EKSEKUSI (Jika semua validasi lolos) ---
        
        # 1. Menambah perolehan suara pada kandidat yang dipilih
        self.daftar_kandidat[id_kandidat].jumlah_suara += 1
        
        # 2. MENGUNCI STATUS PEMILIH: Mengubah False menjadi True
        # Ini adalah bagian terpenting agar validasi nomor 2 bekerja di masa depan
        pemilih.sudah_memilih = True
        
        return True, "Sukses"