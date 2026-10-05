def hitung_nilai(*args):
    rata_rata = sum(args) / len(args)
    nilai_tertinggi = max(args)
    nilai_terendah = min(args)
    return rata_rata, nilai_tertinggi, nilai_terendah


def ubah_nilai(teks):
    try:
        return int(teks)
    except ValueError:
        return float(teks)
    
daftar_nilai = []

while True:
    nilai_input = input("Masukkan nilai ujian siswa (kosongkan untuk selesai): ")
    
    if nilai_input == "":
        break
    

    daftar_nilai.append(ubah_nilai(nilai_input))

if daftar_nilai:
    rata_rata, tertinggi, terendah = hitung_nilai(*daftar_nilai)
    print(f"Rata-rata kelas: {rata_rata}")
    print(f"Nilai tertinggi: {tertinggi}")
    print(f"Nilai terendah: {terendah}")
else:
    print("Data nilai tidak tersedia.")