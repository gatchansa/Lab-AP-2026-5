import re


def bersihkan(nomor):
    return re.sub(r"[ -]", "", nomor)

def cek_nomor(nomor):
    return re.match(r"^[0-9]{10,13}$", nomor)

print("=== Pembersihan Data Nomor Telepon ===")
print()

while True:
    teks = input("Masukkan jumlah data: ")

    if not re.match(r"^[0-9]+$", teks):
        print("Input harus berupa angka!")
        continue

    jumlah = int(teks)

    if jumlah == 0:
        print("Jumlah data harus lebih dari 0!")
        continue

    break
print()

data_sebelum = []
for i in range(1, jumlah + 1):
    nomor = input(f"Nomor ke-{i}: ")
    data_sebelum.append(nomor)
    print()

data_sesudah = []
nomor_valid = []

print("--- Hasil Pembersihan ---")
print()

for i in range(jumlah):
    bersih = bersihkan(data_sebelum[i])
    data_sesudah.append(bersih)

    print(f"Data {i + 1}:")
    print(f"Sebelum : {data_sebelum[i]}")
    print(f"Sesudah : {bersih}")

    if cek_nomor(bersih):
        nomor_valid.append(bersih)
        print("Status  : Valid")
    else:
        print("Status  : Tidak valid")
    print()

print(f"Jumlah nomor valid: {len(nomor_valid)}")