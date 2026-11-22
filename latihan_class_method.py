class Mahasiswa:
    nim = 6447847
    nama = ""

    def perkenalan(self):
        print(f"Halo nama saya {self.nama}")


mahasiswa = Mahasiswa()
mahasiswa.nama = "Fahrul"
mahasiswa.perkenalan()