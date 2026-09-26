print("--- Sistem Reservasi PO BUS ---")

# input jumlah kursi bus
while True:
    try:
        jum_kursi = int(input("Masukkan maksimal kursi bus: "))
    except:
        print("Input jumlah kursi harus berupa angka!")
        continue

    if jum_kursi <= 0:
        print("Jumlah kursi harus lebih dari 0!")
        continue

    break

print()
print("--- Sistem Reservasi PO BUS Dimulai ---")
print()

total_pendapatan = 0

# kuota kursi
while jum_kursi > 0:
    print(f"Sisa kursi: {jum_kursi}")

    try:
        umur = int(input("Masukkan umur penumpang: "))
    except:
        print("Input umur harus berupa angka!")
        print()
        continue

    if umur < 0:
        print("Umur tidak valid!")
        print()
        continue

    # syarat umur dan harga tiket
    if 0 <= umur <= 5:
        kategori = "Balita"
        harga = 0
    elif 6 <= umur <= 12:
        kategori = "Anak"
        harga = 50000
    else:
        kategori = "Dewasa"
        harga = 100000

    # info kategori tiket
    if harga == 0:
        print(f"Kategori: {kategori} - Tiket Gratis (Rp {harga})")
    else:
        print(f"Kategori: {kategori} - Harga: Rp {harga}")

    # kurangi sisa kursi dan tambahkan harga ketika tiket berhasil
    total_pendapatan = total_pendapatan + harga
    jum_kursi = jum_kursi - 1
    print()

print("--- Semua Kursi Terisi ---")
print(f"Total pendapatan perjalanan PO BUS kali ini: Rp {total_pendapatan}")