# TUPRAAAAKKK

menu = ["Kopi Susu", "Matcha Latte", "Americano"]
harga = [18000, 22000, 15000]
jumlah = [4, 3, 5]

# TENTUKAN SUBTOTAL KOPSU, MATCHA DAN AMER
sub_kopsu = harga[0] * jumlah[0]
sub_matcha = harga[1] * jumlah[1]
sub_amer = harga [2] * jumlah[2]

# MASUKKAN SUBTOTAL KE LIST TERBARU (subtotal_pendapatan)
subtotal_pendapatan = [sub_kopsu, sub_matcha, sub_amer]

# HITUNG TOTAL KESELURUHAN
total_seluruh = sub_kopsu + sub_matcha + sub_amer

# HITUNG PENDAPATAN BERSIH
BIAYA_OPERASIONAL = 15000
pendapatan_bersih = total_seluruh - BIAYA_OPERASIONAL

# TOTAL MENU TERJUAL
total_menu = jumlah [0] + jumlah [1] + jumlah [2]

# CEK TARGET
target_tercapai = pendapatan_bersih > 200000 and total_menu > 10

print("Subtotal Kopi Susu:", sub_kopsu)
print("Subtotal Matcha Latte:", sub_matcha)
print("Subtotal Americano:", sub_amer)
print("Pendapatan Bersih", pendapatan_bersih)
print("Hasil target", target_tercapai)
print(total_seluruh)
print(total_menu)