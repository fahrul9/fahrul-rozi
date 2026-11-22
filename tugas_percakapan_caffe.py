
class Pelanggan:
    def __init__(self, nama):
        self.nama = nama

    def berbicara(self, pesan):
        print(f"{self.nama}: {pesan}")


# Membuat objek
topik = Pelanggan("Topik")
fahrul = Pelanggan("Fahrul")

print("=== PERCAKAPAN DI KAFE ===\n")

topik.berbicara("Hai Fahrul, mau pesan minuman apa?")
fahrul.berbicara("Saya mau pesan kopi susu.")
topik.berbicara("Kalau saya mau pesan Americano.")
fahrul.berbicara("Kafe ini nyaman juga ya.")
topik.berbicara("Iya, cocok untuk nongkrong dan mengerjakan tugas.")
fahrul.berbicara("Bagaimana tugas Python kamu?")
topik.berbicara("Lumayan, masih belajar memahami coding.")
fahrul.berbicara("Sama, kita belajar bersama saja.")
topik.berbicara("Setuju! Setelah ini kita kerjakan tugas.")
fahrul.berbicara("Oke, ayo kita mulai!")

print("\n=== PERCAKAPAN SELESAI ===")
