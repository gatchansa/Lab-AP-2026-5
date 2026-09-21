persentase = int(input("Masukkan persentase cabai: "))

if persentase < 0:
    print("Input tidak valid")
elif persentase <= 10:
    print("Level Aman")
elif persentase <= 40:
    print("Level Sedang")
elif persentase <= 70:
    print("Level Pedas")
else:
    print("Level Ekstrem")

