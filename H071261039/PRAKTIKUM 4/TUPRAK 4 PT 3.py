def hitung_mundur(angka):
    print(angka)

    if angka == 0:
        print("Luncurkan!")
        return

    hitung_mundur(angka - 1)


while True:
    angka_awal = input("Masukkan angka awal hitung mundur: ")
    angka_awal = int(angka_awal)

    if angka_awal < 0:
        print("Input tidak valid, angka tidak boleh negatif.")
        continue

    break 

hitung_mundur(angka_awal)