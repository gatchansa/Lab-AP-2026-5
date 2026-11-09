class Pemain:
    def __init__(self, nama, id_pemain, role, nilai_kill, nilai_assist, nilai_objective):
        self.nama = nama
        self.id_pemain = id_pemain
        self.role = role
        self.nilai_kill = nilai_kill
        self.nilai_assist = nilai_assist
        self.nilai_objective = nilai_objective

    def hitung_skor_akhir(self):
        skor = (0.3 * self.nilai_kill) + (0.3 * self.nilai_assist) + (0.4 * self.nilai_objective)
        return skor

    def status_performa(self):
        # round(..., 2) agar angka desimal komputer tidak membuat skor 60 terbaca 59.99999
        if round(self.hitung_skor_akhir(), 2) >= 60:
            return "Unggul"
        else:
            return "Perlu Evaluasi"

    def tampilkan_data(self, no):
        skor = self.hitung_skor_akhir()
        status = self.status_performa()
        print(f"| {no:<2} | {self.nama:<6} | {self.id_pemain:<10} | {self.role:<8} | {skor:<10.2f} | {status:<15} |")

def minta_nilai(pesan):
    while True:
        try:
            nilai = float(input(pesan))
        except ValueError:
            print("Input harus berupa angka!")
            continue

        if nilai < 0:
            print("Nilai tidak boleh negatif!")
            continue

        return nilai


print("=== SISTEM PENILAIAN PERFORMA PEMAIN ===")
print()

jumlah = int(input("Masukkan jumlah pemain: "))
print()

daftar_pemain = []  # list untuk menyimpan objek Pemain

for i in range(1, jumlah + 1):
    print(f"-- Data Pemain ke-{i} --")
    nama = input("Nama: ")

    while True:
        id_pemain = input("ID Pemain: ")

        sudah_ada = False
        for p in daftar_pemain:
            if p.id_pemain.lower() == id_pemain.lower():  
                sudah_ada = True

        if sudah_ada:
            print("ID Pemain sudah digunakan!")
        else:
            break

    role = input("Role: ")
    nilai_kill = minta_nilai("Nilai Kill: ")
    nilai_assist = minta_nilai("Nilai Assist: ")
    nilai_objective = minta_nilai("Nilai Objective: ")

    pemain = Pemain(nama, id_pemain, role, nilai_kill, nilai_assist, nilai_objective)
    daftar_pemain.append(pemain)
    print()

garis = "=" * 70

print("=== REKAPITULASI PERFORMA PEMAIN ===")
print(garis)
print("| No | Nama   | ID Pemain  | Role     | Skor Akhir | Status          |")
print(garis)

nomor = 1
for pemain in daftar_pemain:
    pemain.tampilkan_data(nomor)
    nomor += 1

print(garis)