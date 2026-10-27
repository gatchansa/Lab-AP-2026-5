import os
import random
from datetime import datetime


FOLDER_INVOICE = "invoices"
FILE_RIWAYAT = "invoices.txt"


# Tampilan tabel riwayat (sama persis dengan contoh di soal)
GARIS_TABEL = "=" * 66
HEADER_TABEL = "|        Waktu        |   ID Transaksi    |  Nominal Transaksi   |"


def minta_teks(pesan):
    """Minta teks yang tidak boleh kosong."""
    while True:
        teks = " ".join(input(pesan).split())  
        if teks:
            return teks
        print("Input tidak boleh kosong!")


def minta_nama_kasir():
    while True:
        nama = minta_teks("Nama kasir: ")
        ada_huruf = False
        for karakter in nama:
            if karakter.isalpha():
                ada_huruf = True
        if ada_huruf:
            return nama
        print("Nama kasir harus mengandung huruf!")


def minta_angka(pesan):
    while True:
        teks = input(pesan).strip()
        try:
            angka = int(teks)
        except ValueError:
            print("Input harus berupa angka!")
            continue

        if angka <= 0:
            print("Angka harus lebih dari 0!")
        else:
            return angka


def minta_ya_tidak(pesan):
    while True:
        jawab = input(pesan).strip().lower()
        if jawab in ("y", "ya"):
            return True
        if jawab in ("n", "t", "tidak"):
            return False
        print("Ketik 'y' untuk ya atau 't' untuk tidak!")

def buat_inisial(nama):
    kata_kata = []
    for kata in nama.split():
        huruf = ""
        for karakter in kata:
            if karakter.isalpha():
                huruf += karakter
        if huruf:
            kata_kata.append(huruf)

    if len(kata_kata) == 1:
        return kata_kata[0][:3].upper()

    inisial = ""
    for kata in kata_kata:
        inisial += kata[0]
    return inisial.upper()


def file_sudah_ada(path):
    try:
        with open(path, "r", encoding="utf-8"):
            return True
    except FileNotFoundError:
        return False


def buat_id_transaksi(nama_kasir, waktu):
    awal = buat_inisial(nama_kasir) + waktu.strftime("%y%m%d%H%M")

    for angka_acak in random.sample(range(100, 1000), 900):
        id_transaksi = awal + str(angka_acak)
        path = os.path.join(FOLDER_INVOICE, id_transaksi + ".txt")
        if not file_sudah_ada(path):
            return id_transaksi

    raise RuntimeError("Semua ID untuk menit ini sudah terpakai. Coba lagi sebentar lagi.")


def simpan_invoice(id_transaksi, waktu, nama_kasir, daftar_item, total):
    """buat file invoice <ID>.txt di folder 'invoices'."""
    os.makedirs(FOLDER_INVOICE, exist_ok=True) 
    path = os.path.join(FOLDER_INVOICE, id_transaksi + ".txt")

    garis_tebal = "=" * 46
    garis_tipis = "-" * 46

    with open(path, "w", encoding="utf-8") as file:
        file.write(garis_tebal + "\n")
        file.write("INVOICE / STRUK BELANJA".center(46) + "\n")
        file.write(garis_tebal + "\n")
        file.write(f"ID Transaksi : {id_transaksi}\n")
        file.write(f"Waktu        : {waktu.strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write(f"Kasir        : {nama_kasir}\n")
        file.write(garis_tipis + "\n")

        nomor = 1
        for item in daftar_item:
            subtotal = item["harga"] * item["jumlah"]
            file.write(f"{nomor}. {item['nama']}\n")
            file.write(f"   Rp. {item['harga']} x {item['jumlah']} = Rp. {subtotal}\n")
            nomor += 1

        file.write(garis_tipis + "\n")
        file.write(f"TOTAL        : Rp. {total}\n")
        file.write(garis_tebal + "\n")

    return path


def simpan_riwayat(waktu, id_transaksi, total):
    """
    1. Baca isi trx_history.txt (jika sudah ada).
    2. Ubah isinya: buang garis penutup lama, tambah baris transaksi baru,
       pasang garis penutup lagi.
    3. Tulis kembali ke file.
    """
    waktu_teks = waktu.strftime("%Y-%m-%d %H:%M:%S")
    nominal = "Rp. " + str(total)
    baris_baru = f"| {waktu_teks:<19} | {id_transaksi:<17} | {nominal:<20} |"

    # 1. Membaca isi lama (jika file belum ada, anggap kosong)
    try:
        with open(FILE_RIWAYAT, "r", encoding="utf-8") as file:
            isi = file.read().splitlines()
    except FileNotFoundError:
        isi = []

    # 2. Mengubah isi
    if not isi:
        isi = [GARIS_TABEL, HEADER_TABEL, GARIS_TABEL]  # file baru -> buat header
    elif isi[-1] == GARIS_TABEL and len(isi) > 3:
        isi.pop()  # buang garis penutup lama
    isi.append(baris_baru)
    isi.append(GARIS_TABEL)

    # 3. Menulis kembali
    with open(FILE_RIWAYAT, "w", encoding="utf-8") as file:
        file.write("\n".join(isi) + "\n")


# ============================================================
# FITUR 1: TRANSAKSI BARU
# ============================================================
def transaksi_baru():
    print("\n--- Transaksi Baru ---")
    nama_kasir = minta_nama_kasir()

    daftar_item = []
    while True:
        print(f"\nProduk ke-{len(daftar_item) + 1}")
        nama_produk = minta_teks("Nama produk: ")
        harga = minta_angka("Harga produk: ")
        jumlah = minta_angka("Jumlah produk yang dibeli: ")

        daftar_item.append({"nama": nama_produk, "harga": harga, "jumlah": jumlah})
        print(f"Subtotal {nama_produk}: Rp. {harga * jumlah}")

        if not minta_ya_tidak("Tambah produk lagi? (y/n): "):
            break
        
    total = 0
    for item in daftar_item:
        total += item["harga"] * item["jumlah"]
    waktu = datetime.now()

    try:
        id_transaksi = buat_id_transaksi(nama_kasir, waktu)
        path_invoice = simpan_invoice(id_transaksi, waktu, nama_kasir, daftar_item, total)
    except (OSError, RuntimeError) as error:
        print(f"\nGagal membuat invoice: {error}")
        return

    try:
        simpan_riwayat(waktu, id_transaksi, total)
    except OSError as error:
        print(f"\nInvoice tersimpan, tetapi gagal mencatat riwayat: {error}")

    print("\nTransaksi berhasil!")
    print(f"ID Transaksi  : {id_transaksi}")
    print(f"Total belanja : Rp. {total}")
    print(f"Invoice disimpan di: {path_invoice}")

def cari_invoice():
    print("\n--- Cari Invoice ---")
    id_transaksi = input("Masukkan ID transaksi: ").strip().upper()

    if id_transaksi.endswith(".TXT"):  # jika tidak sengaja menulis .txt
        id_transaksi = id_transaksi[:-4]

    if not id_transaksi:
        print("ID transaksi tidak boleh kosong!")
        return

    if not id_transaksi.isalnum():
        print("Format ID transaksi tidak valid!")
        return

    path = os.path.join(FOLDER_INVOICE, id_transaksi + ".txt")

    # READING: hanya membaca & menampilkan, TIDAK membuat/mencetak ulang invoice
    try:
        with open(path, "r", encoding="utf-8") as file:
            isi = file.read()
    except FileNotFoundError:
        print(f"Invoice dengan ID {id_transaksi} tidak ditemukan!")
        return
    except OSError as error:
        print(f"Gagal membaca invoice: {error}")
        return

    print(f"\nInvoice {id_transaksi} ditemukan:\n")
    print(isi)

def lihat_riwayat():
    print("\n--- Riwayat Transaksi ---")
    try:
        with open(FILE_RIWAYAT, "r", encoding="utf-8") as file:
            isi = file.read()
    except FileNotFoundError:
        print("Belum ada transaksi yang tercatat.")
        return
    except OSError as error:
        print(f"Gagal membaca riwayat: {error}")
        return

    print(isi)

def main():
    print("=== Aplikasi Kasir ===")
    while True:
        print("\nMenu:")
        print("1. Transaksi baru")
        print("2. Cari invoice")
        print("3. Lihat riwayat transaksi")
        print("4. Keluar")
        pilihan = input("Pilih menu (1-4): ").strip()

        if pilihan == "1":
            transaksi_baru()
        elif pilihan == "2":
            cari_invoice()
        elif pilihan == "3":
            lihat_riwayat()
        elif pilihan == "4":
            print("Terima kasih. Program selesai.")
            break
        else:
            print("Pilihan tidak valid! Masukkan angka 1 sampai 4.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nProgram dihentikan. Terima kasih.")
