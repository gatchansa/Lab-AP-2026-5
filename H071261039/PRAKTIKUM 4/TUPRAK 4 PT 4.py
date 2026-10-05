def konversi_suhu(suhu, skala_asal, skala_tujuan):
    
    skala_asal = skala_asal.upper()
    skala_tujuan = skala_tujuan.upper()

    if skala_asal not in ("C", "F", "K") or skala_tujuan not in ("C", "F", "K"):
        raise ValueError("Skala suhu tidak dikenali.")

    # Langkah 1: ubah suhu asal menjadi Celsius terlebih dahulu
    if skala_asal == "C":
        celsius = suhu
    elif skala_asal == "F":
        celsius = (suhu - 32) * 5 / 9
    else:  # K
        celsius = suhu - 273.15

    # Langkah 2: ubah dari Celsius ke skala tujuan
    if skala_tujuan == "C":
        hasil = celsius
    elif skala_tujuan == "F":
        hasil = int(celsius * 9 / 5 + 32)
    else:  # K
        hasil = int(celsius + 273.15)

    return hasil


print("=== Konversi Suhu ===")

while True:
    suhu_input = input("Masukkan suhu (atau 'selesai' untuk keluar): ")

    if suhu_input.lower() == "selesai":
        break

    suhu = float(suhu_input)
    skala_asal = input("Skala asal (C/F/K): ")
    skala_tujuan = input("Skala tujuan (C/F/K): ")

    try:
        hasil = konversi_suhu(suhu, skala_asal, skala_tujuan)
        print(f"Hasil: {suhu} {skala_asal.upper()} = {hasil} {skala_tujuan.upper()}")
    except ValueError as e:
        print(f"Error: {e}")