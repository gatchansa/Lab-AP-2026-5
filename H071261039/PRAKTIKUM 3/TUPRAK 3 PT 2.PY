print("--- Setup Denah Bioskop NontonYuk ---")

# input jumlah baris
while True:
    try:
        jumlah_baris = int(input("Masukkan jumlah baris: "))
    except:
        print("Input baris harus berupa angka!")
        print()
        continue

    if jumlah_baris <= 0:
        print("Jumlah baris harus lebih dari 0!")
        print()
        continue

    break

# input jumlah kursi per baris
while True:
    try:
        jumlah_kursi = int(input("Masukkan jumlah kursi: "))
    except:
        print("Input kursi harus berupa angka!")
        print()
        continue

    if jumlah_kursi <= 0:
        print("Jumlah kursi harus lebih dari 0!")
        print()
        continue

    break

print()
print("--- Daftar Kursi Tersedia ---")


for baris in range(1, jumlah_baris + 1):
    for kursi in range(1, jumlah_kursi + 1):

        # Aturan Mitos (ga boleh 13)
        if kursi == 13:
            continue

        # Aturan Baris VVIP (ganjil)
        if baris == 1 and kursi % 2 == 0:
            continue

        # Baris 2 dan seterusnya: semua kursi (kecuali 13) tampil normal
        print(f"Baris {baris} - Kursi {kursi}")