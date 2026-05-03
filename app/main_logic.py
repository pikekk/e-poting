class Pemilih:
    def __init__(self, id_pemilih, nama):
        self.id_pemilih = id_pemilih
        self.nama = nama
        self.sudah_memilih = False

class Kandidat:
    def __init__(self, id_kandidat, nama):
        self.id_kandidat = id_kandidat
        self.nama = nama
        self.jumlah_suara = 0

class SistemEVoting:
    def __init__(self):
        self.daftar_pemilih = {}
        self.daftar_kandidat = {}

    def tambah_pemilih(self, id_pemilih, nama):
        self.daftar_pemilih[id_pemilih] = Pemilih(id_pemilih, nama)

    def tambah_kandidat(self, id_kandidat, nama):
        self.daftar_kandidat[id_kandidat] = Kandidat(id_kandidat, nama)

    def voting(self, id_pemilih, id_kandidat):
        if id_pemilih not in self.daftar_pemilih:
            return False, "ID Tidak Terdaftar"
        pemilih = self.daftar_pemilih[id_pemilih]
        if pemilih.sudah_memilih:
            return False, "Sudah Memilih"
        if id_kandidat not in self.daftar_kandidat:
            return False, "Kandidat Tidak Ada"
        
        self.daftar_kandidat[id_kandidat].jumlah_suara += 1
        pemilih.sudah_memilih = True
        return True, "Sukses"