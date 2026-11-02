import re


def cek_nim(nim):
    return re.match(r"^H071[0-9]{6}$", nim)

def cek_email(email):
    return re.match(r"^[A-Za-z0-9._]+@[A-Za-z0-9]+\.[A-Za-z]+$", email)

def cek_telepon(telepon):
    return re.match(r"^[0-9]{10,13}$", telepon)


print("=== Validasi Data Mahasiswa ===")
print()

nim = input("Masukkan NIM      : ")
email = input("Masukkan Email    : ")
telepon = input("Masukkan No. Telp : ")

print()
print("--- Hasil Validasi ---")

semua_valid = True

if cek_nim(nim):
    print("NIM         : Valid")
else:
    print("NIM         : Format NIM tidak valid!")
    semua_valid = False

if cek_email(email):
    print("Email       : Valid")
else:
    print("Email       : Format email tidak valid!")
    semua_valid = False

if cek_telepon(telepon):
    print("No. Telepon : Valid")
else:
    print("No. Telepon : Nomor telepon tidak valid!")
    semua_valid = False

if semua_valid:
    print()
    print("Data mahasiswa berhasil diverifikasi!")