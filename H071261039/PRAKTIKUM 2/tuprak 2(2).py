jarak = int(input("Masukkan Jarak Pengiriman (km): "))
express = input("Layanan Express (ya/tidak): ")

if jarak < 5:
    tarif = 10000
elif jarak <= 20:
    tarif = 20000
else:
    tarif = 35000

biaya_tambahan = 15000 if express == "ya" else 0
total = tarif + biaya_tambahan

print("Total tarif pengiriman: Rp", total)