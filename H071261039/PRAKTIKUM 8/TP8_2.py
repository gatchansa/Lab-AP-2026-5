import re

def cek_username(username):
    return re.match(r"^[A-Za-z][A-Za-z0-9_]{4,11}$", username)


print("=== Registrasi Username ===")
print("Ketik 'SELESAI' untuk mengakhiri.")
print()

daftar_valid = []

while True:
    username = input("Masukkan username: ")

    if username == "SELESAI":
        break

    if cek_username(username):
        daftar_valid.append(username)
        print("Username tersedia.")
    else:
        print("Username tidak valid!")
    print()

print()
print("=== Rekapitulasi ===")
print("Username valid:")

nomor = 1
for nama in daftar_valid:
    print(f"{nomor}. {nama}")
    nomor += 1

print()
print(f"Jumlah username valid: {len(daftar_valid)}")