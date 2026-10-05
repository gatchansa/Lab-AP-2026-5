def hitung_subtotal(harga, jumlah, is_member=False):
   
    subtotal = harga * jumlah
    if is_member:
        subtotal = subtotal * 0.9 
    return subtotal

print("Selamat datang di Kasir Minimarket!")
status = input("Apakah Anda member? (y/n): ")
is_member = status.lower() == "y"

total_belanja = 0

while True:
    nama_barang = input("Masukkan nama barang (kosongkan untuk selesai): ")

    if nama_barang == "":
        break

    harga = int(input("Harga barang: "))
    jumlah = int(input("Jumlah barang: "))

    subtotal = hitung_subtotal(harga, jumlah, is_member)
    print(f"Subtotal {nama_barang}: Rp{int(subtotal)}")

    total_belanja += subtotal

print(f"Total belanja: Rp{int(total_belanja)}")