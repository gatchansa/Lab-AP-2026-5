tujuan = input("Masukkan Tujuan (Pantai/Pegunungan/Kota): ")
waktu = input("Masukkan Waktu (Pagi/Malam): ")
tipe = input("Masukkan Tipe Pengunjung (Anak/Dewasa): ")

match tujuan:
    case "pantai":
        if waktu == "pagi":
            rekomendasi = "Paket A"
        elif waktu == "malam" and tipe == "dewasa":
            rekomendasi = "Paket C"
        else:
            rekomendasi = "Tidak ada paket yang cocok"

    case "pegunungan":
        if waktu == "pagi" and tipe == "dewasa":
            rekomendasi = "Paket B"
        elif waktu == "malam" and tipe == "dewasa":
            rekomendasi = "Paket C"
        else:
            rekomendasi = "Tidak ada paket yang cocok"

    case "kota":
        if waktu == "malam":
            rekomendasi = "Paket C"
        else:
            rekomendasi = "Tidak ada paket yang cocok"

    case _:
        rekomendasi = "Tidak ada paket yang cocok"

print("Paket Rekomendasi: ", rekomendasi)