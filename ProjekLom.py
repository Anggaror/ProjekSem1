donasi = {}

def tampilkan_donasi(): # done gak bang? done
    if not donasi:
        print("\nBelum ada donasi tercatat.")
    else:
        print("\n=== DAFTAR DONASI ===")
        for nama, data in donasi.items():
            print(f"- {nama}: Rp {data[0]:,} | Kategori: {data[1]} | Metode: {data[2]} | Tanggal: {data[3]}")


def tambah_donasi(): # punya angga
    while True: # done
        nama = input("Masukkan nama donatur: ")
        if not nama.replace(" ", "").isalpha():
            print("Nama hanya boleh huruf dan tidak boleh kosong!")
            continue
        if nama in donasi:
            print("Nama sudah ada! Gunakan update.")
            continue
        break

    while True: # done
        jumlah = input("Masukkan jumlah donasi (Rp): ")
        if jumlah.isalpha():  
            print("Nominal harus berupa angka!")
            continue

        jumlah = int(jumlah)
        if jumlah <= 0:
            print("Nominal tidak boleh minus")
            continue

        elif jumlah <= 100:
            print("Nominal tidak boleh kurang dari Rp.100, coba lagi!")
            continue
        break

    while True: # done
        tgl = input("Masukkan tanggal (1-31): ")
        if not tgl.isdigit():
            print("Tanggal hanya boleh angka!")
            continue

        tgl = int(tgl)
        if not (1 <= tgl <= 31):
            print("Tanggal harus 1–31!")
            continue
        break

    while True: # done
        bln = input("Masukkan bulan (1-12): ")
        if not bln.isdigit():
            print("Bulan hanya boleh angka!")
            continue

        bln =  int(bln)
        if not (1<= bln <=12):
            print("Bulan harus 1-12")
            continue
        break

    while True: # done
        thn = input("Masukkan tahun: ")
        if not thn.isdigit():
            print("Tahun hanya boleh angka!")
            continue

        thn = int(thn)
        if thn < 2025:
            print("Tidak boleh kurang dari 2025")
            continue
        break

    tanggal = f"{tgl}-{bln}-{thn}"   

    kategori_pilihan = {
        "1": "Bencana Alam",
        "2": "Pendidikan",
        "3": "Sosial",
        "4": "Pembangunan"
    }

    print("\nPilih kategori:")
    print("1. Bencana Alam")
    print("2. Pendidikan")
    print("3. Sosial")
    print("4. Pembangunan")

    while True: # done
        p = input("Pilih kategori (1-4): ")
        if p not in kategori_pilihan:
            print("Pilihan tidak valid!")
            continue
        kategori = kategori_pilihan[p]
        break

    metode_pilihan = {
        "1": "Transfer Bank",
        "2": "E-Wallet",
        "3": "QRIS"
    }

    print("\nPilih metode:")
    print("1. Transfer Bank")
    print("2. E-Wallet")
    print("3. QRIS")

    while True: # done
        m = input("Pilih metode (1-3): ")
        if m not in metode_pilihan:
            print("Pilihan tidak valid!")
            continue
        metode = metode_pilihan[m]
        break

    donasi[nama] = [jumlah, kategori, metode, tanggal]
    print("Donasi berhasil ditambahkan!")

def cari_donasi(): # done, kurg dikit (rapiin dict)
    if nama not in donasi:
        print("Tidak ditemukan.")
        return
    
    while True:
        nama = input("Masukkan nama donatur yang ingin dicari: ")
        if not nama.replace(" ", "").isalpha():
            print("Nama tidak boleh mengandung angka dan tidak boleh kosong!")
            continue
        elif nama in donasi:
            print("Ditemukan:", donasi[nama])
        break 

def update_donasi(): # ada ide tapi lom diubah (try-except buat input jumlah, inf loop, validasi ++)
    while True:
        nama = input("Masukkan nama donatur yang akan diperbarui: ")
        if nama not in donasi:
            print("Donatur tidak ada.")
            continue

        try: # nyampe sini
            jumlah_baru = input("Masukkan jumlah donasi baru: ")
        # except:
        #     if jumlah_baru.isalpha():

            
        except:
            print("Input salah, update dibatalkan.")
            return
        break

    donasi[nama][0] = jumlah_baru
    print("Donasi diperbarui.")


def hapus_donasi(): # simple (ks inf loop, validasi ++)
    nama = input("Masukkan nama donatur: ")
    if nama in donasi:
        del donasi[nama]
        print("Dihapus.")
    else:
        print("Tidak ditemukan.")


def total_donasi():# lom (operator/function sum)
    print("Fitur total donasi belum selesai.")


def sorting_donasi(): # lom (Ascending, Descending)
    print("Fitur sorting belum tersedia.")


def menu(): # done
    while True:
        print("\n=== MENU DONASI ONLINE ===")
        print("1. Tampilkan Donasi")
        print("2. Tambah Donasi")
        print("3. Cari Donasi")
        print("4. Update Donasi")
        print("5. Hapus Donasi")
        print("6. Total Donasi")
        print("7. Sorting Donasi")
        print("8. Keluar")

        pilihan = input("Pilih menu (1-8): ")

        if pilihan == "1":
            tampilkan_donasi()
        elif pilihan == "2":
            tambah_donasi()
        elif pilihan == "3":
            cari_donasi()
        elif pilihan == "4":
            update_donasi()
        elif pilihan == "5":
            hapus_donasi()
        elif pilihan == "6":
            total_donasi()
        elif pilihan == "7":
            sorting_donasi()
        elif pilihan == "8":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid.")
            continue

menu()
