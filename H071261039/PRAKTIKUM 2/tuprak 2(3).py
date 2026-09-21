nilai = int(input("Masukkan Nilai tes: "))
pengalaman = int(input("Masukkan Pengalaman Kerja (tahun): "))

if nilai >= 80:
    status = "Lolos ke Tahap Wawancara"
elif nilai >= 65 and pengalaman >= 2:
    status = "Lolos Bersyarat"
else:
    status = "Tidak Lolos"

print(status)