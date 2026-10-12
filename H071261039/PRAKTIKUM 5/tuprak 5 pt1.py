huruf = "abcdefghijklmnopqrstuvwxyz"

def bersihkan_teks(text):
    simpan = ""
    for i in text:
        if i in huruf:
            simpan += i
    return simpan

def cek_palindrome(text):
    teks_terbalik = "".join(reversed(text))
    panjang_teks = len(text)
    for i in range(panjang_teks):
        if text[i] != teks_terbalik[i]:
            return (False, i)
    return (True, -1)

def inti_palindrome(text):
    indeks_awal = -1
    teks_bersih = bersihkan_teks(text)
    palindrome_terpanjang = ""
    panjang_teks = len(teks_bersih)
    for i in range(panjang_teks):
        for j in range(i + 1, panjang_teks + 1):
            potongan = teks_bersih[i:j]
            palindrome = cek_palindrome(potongan)[0]
            if palindrome:
                if len(potongan) > len(palindrome_terpanjang):
                    palindrome_terpanjang = potongan
                    indeks_awal = i
    return {
        "teks": palindrome_terpanjang,
        "panjang": len(palindrome_terpanjang),
        "indek_awal": indeks_awal
    }

input_kata = input("Masukkan teks prasasti: "). lower()
tes = inti_palindrome(input_kata)
bersih = bersihkan_teks(input_kata)
print(f"Teks Bersih: {bersih}")
print(f"Output Terharap: {tes}")