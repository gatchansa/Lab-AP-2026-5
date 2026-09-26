print("--- Rekapitulasi Transaksi Dins Store ---")
print("Ketik '0' untuk menutup toko dan mengakhiri sesi.")
print()

while True:
    # input berupa angka
    try:
        jumlah = int(input("Masukkan jumlah item: "))
    except:
        print("Input harus berupa angka!")
        print()
        continue

    if jumlah < 0:
        print("Jumlah tidak boleh negatif")
        print()
        continue

    if jumlah > 100:
        print("Maksimal 100 item per transaksi!")
        print()
        continue

    if jumlah == 0:
        print("Toko ditutup. Sesi rekap selesai.")
        break

    print(f"Transaksi {jumlah} item berhasil!")
    print()