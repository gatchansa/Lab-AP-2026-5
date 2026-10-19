print("SHALX")
judul_nya = list()
artis_nya = list()
genre_nya = set()
durasi_nya = list()
lagu_dan_genre = {}
genre_dan_total = {}
genre = ["Pop", "Rock", "Jazz", "RnB", "Dangdut"]

def tambah_lagu(playlist, genre_set, judul, artis, genre, durasi):
    genre_dan_total[genre_set] = 0
    lagu_dan_genre[playlist] = genre_set
    judul_nya.append(judul)
    artis_nya.append(artis)
    genre_nya.add(genre)
    durasi_nya.append(durasi)
    genre_dan_total[genre_set] += 1
    return lagu_dan_genre, judul_nya, artis_nya, genre_nya, durasi_nya, genre_dan_total

def  tampilkan_playlist(playlist):
    total_durasi_menit = sum(durasi_nya) // 60
    total_durasi_detik = sum(durasi_nya) % 60
    baris_ke = 1
    ada_berapa_judul = len(judul_nya)
    judul_terpanjang = max(len(i) for i in judul_nya)
    artis_terpanjang = max(len(i) for i in artis_nya)
    genre_terpanjang = max(len(i) for i in genre)
    durasi_terpanjang_str = [len(str(i)) for i in durasi_nya]
    durasi_terpanjang = max(durasi_terpanjang_str)
    print(f"====={judul_terpanjang * "=" }=={artis_terpanjang * "=" }=={genre_terpanjang * "=" }==={durasi_terpanjang * "=" }=")
    print(f" No  Judul{(judul_terpanjang - 5) * " "}  Artis{(artis_terpanjang - 5) * " "}  Genre{(genre_terpanjang - 5) * " "}   Durasi")
    print(f"====={judul_terpanjang * "=" }=={artis_terpanjang * "=" }=={genre_terpanjang * "=" }==={durasi_terpanjang * "=" }=")
    for i in range(ada_berapa_judul):
        untuk_genre = judul_nya[i]
        menit = durasi_nya[i] // 60
        detik = durasi_nya[i] % 60
        print(f" {baris_ke}   {judul_nya[i].ljust(judul_terpanjang)}  {artis_nya[i].ljust(artis_terpanjang)}  {lagu_dan_genre[untuk_genre].ljust(genre_terpanjang)}   {menit}:{detik}")
        baris_ke += 1
    print(f"====={judul_terpanjang * "=" }=={artis_terpanjang * "=" }=={genre_terpanjang * "=" }==={durasi_terpanjang * "=" }=")
    print(f"Total durasi playlist: {total_durasi_menit} menit {total_durasi_detik} detik")
    print()

def filter_genre(playlist, genre_target):
    print(f"Lagu bergenre '{genre_target}':")
    urutan = 1
    index = 0
    for key, value in playlist.items():
        if value == genre_target:
            for i in judul_nya:
                if i == key:
                    index = judul_nya.index(i)
            menit = durasi_nya[index] // 60
            detik = durasi_nya[index] % 60
            print(f"  {urutan}. {judul_nya[index]} - {artis_nya[index]} ({menit}:{detik})")
            urutan += 1

def hapus_lagu(playlist, nomor):
    panjang_lagu = len(judul_nya)
    if panjang_lagu < nomor:
        return "Tidak ada lagu pada nomor tersebut/tidak valid"
    nomor_lagu = judul_nya[nomor-1]
    genre_dari_lagu_dihapus = lagu_dan_genre[nomor_lagu]
    lagu_dan_genre.pop(nomor_lagu)
    judul_nya.pop(nomor-1)
    artis_nya.pop(nomor-1)
    durasi_nya.pop(nomor-1)
    for key, value in lagu_dan_genre.items():
        if genre_dari_lagu_dihapus not in value:
            genre_nya.pop(genre_dari_lagu_dihapus)
            genre_dan_total[value] -= 1
            if genre_dan_total[value] == 0:
                genre_dan_total.pop(value)
    print(f"Lagu nomor {nomor} telah berhasil di hapus")
    tampilkan_playlist(playlist)

def statistik_playlist(playlist, genre_dan_total):
    lagu_terpanjang = durasi_nya.index(max(durasi_nya))
    menit_panjang = durasi_nya[lagu_terpanjang] // 60
    detik_panjang = durasi_nya[lagu_terpanjang] % 60
    lagu_terpendek = durasi_nya.index(min(durasi_nya))
    menit_pendek = durasi_nya[lagu_terpendek] // 60
    detik_pendek = durasi_nya[lagu_terpendek] // 60
    print("===============================================")
    print("       STATISTIK PLAYLIST PLAYTUNE")
    print("===============================================")
    print(f"Total lagu        : {len(judul_nya)}")
    print(f"Jumlah genre      : {len(genre_nya)}")
    print(f"Daftar genre      : {genre_nya}")
    print()
    print("Distribusi genre: ")
    for key, value in genre_dan_total.items():
        print(f"  {key}        : # ({value})")
    print()
    print(f"Lagu terpanjang : {judul_nya[lagu_terpanjang]} ({menit_panjang}:{detik_panjang})")
    print(f"Lagu terpanjang : {judul_nya[lagu_terpanjang]} ({menit_pendek}:{detik_pendek})")
    print("===============================================")

print("===============================")
print("   PLAYLIST MUSIK - PLAYTUNE")
print("===============================")
print("Menu:")
print("1. Tambah Lagu")
print("2. Tampilkan Playlist")
print("3. Filter berdasarkan Genre")
print("4. Hapus Lagu")
print("5. Statistik Playlist")
print("6. Keluar")
while True:
    try:
        menu = int(input("Pilih menu (1-6): "))
    except:
        print("Input yang anda masukkan tidak valid")
        continue
    try:
        if menu == 1:
            judul_lagu = input("Judul lagu: ").title ()
            artis_lagu = input("Artis: ").title ()
            genre_lagu = input("(Pop/Rock/Jazz/RnB/Dangdut): ").title ()
            if genre_lagu not in genre:
                print("Genre yang anda masukkan tidak valid")
                continue
            durasi_lagu = int(input("Durasi (dalam detik): "))
            tambah_lagu(judul_lagu, genre_lagu, judul_lagu, artis_lagu, genre_lagu, durasi_lagu)
            print(f"Lagu '{judul_lagu}' oleh {artis_lagu} berhasil ditambahkan!")
            print()
        elif menu == 2:
            print()
            tampilkan_playlist(lagu_dan_genre)
        elif menu == 3:
            print(f"Genre tersedia: {genre_nya}")
            filter_genrenya = input("Masukkan genre yang ingin difilter: ").title ()
            filter_genre(lagu_dan_genre, filter_genrenya)
        elif menu == 4:
            tampilkan_playlist(lagu_dan_genre)
            nomor  = int(input("Masukkan nomor lagu yang ingin di hapus: "))
            hapus_lagu(lagu_dan_genre, nomor)
        elif menu == 5:
            statistik_playlist(lagu_dan_genre, genre_dan_total)
        elif menu == 6:
            print("Terima kasih telah menggunakan PlayTune!")
            break
    except:
        print("Input yang anda masukkan tidak valid")
        continue