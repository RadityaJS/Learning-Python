database = []

while True:
    print(29*"=")
    pilihan = input(f"1. Program Menambahkan Judul Buku Baru\n2. Program Menghapus Buku\n3. Exit\n\npililah jawaban diatas sesuai nomor : ")
    print(29*"=","\n")

    if pilihan == "1":
        while True:
            print(f"--MENAMBAHKAN JUDUL BUKU--")
            print(29*"=")
            judul = input(f"Masukan Judul Buku : ")
            penulis = input(f"Masukan Nama Penulis : ")
            print(29*"=")

            sudah_ada = False
            for data in database:
                if data[0].lower() == judul.lower():
                    sudah_ada = True
                    break

            if sudah_ada:
                print("Buku Sudah ada di dalam Data")
                lanjut = input(f"apakah ingin lanjut menambahkan buku lain? (y/n) : ")
                if lanjut == "n":
                    break
                else:
                    continue

            data_baru = [judul,penulis]
            database.append(data_baru)

            print(f"{'NO':<4} | {'JUDUL BUKU':^25} | {'NAMA PENULIS':^20}")
            print(50*"-")
            for index,data in enumerate(database):
                print(f"{index+1:<4} | {data[0]:<25} | {data[1]:<20}")

            print("\n",29*"=")

            for index,data in enumerate(database):
                print(f"address data {index+1} = {(hex(id(data[1])))}")
                print(f"address data {index+1} = {(hex(id(data[0])))}")    
                print(29*"=") 

            lanjut1 = input(f"Mau Lanjut Menambahkan Buku Lagi? (y/n) : ")

            if lanjut1 == "n":
                break
        print("PROGRAM SELESAI")

    if pilihan == "2":
        print(f"\n--DATA BUKU--")
        if len(database):
            print(f"{'NO':<3} | {'JUDUL BUKU':<25} | {'NAMA PENULIS':<20}")
            print(50*"-")
            for index,data in enumerate(database):
                print(f"{index+1:<3} | {data[0]:<25} | {data[1]:<20}")
        else:
            print("\nData Masih Kosong, tolong di isi dulu!\n")
            continue
        
        print(f"\nJIKA TIDAK JADI MENGHAPUS DATA KETIK HURUF APA AJA")
        hapus = input(f"Masukan No data yang ingin dihapus : ")

        if hapus.isdigit():
            hapus = int(hapus)

            if 1 <= hapus <= len(database):
                buku_hapus = database.pop(hapus - 1)
                print(f"\nData Berhasil dihapus = {buku_hapus}")
            else:
                print(f"Nomor Tidak Valid!")
                continue

        else:
            print("Batal menghapus data, kembali ke menu utama.")
            continue

    if pilihan == "3":
        print(f"PROGRAM SELESAI")
        break


    if pilihan == "Wh1t3r0s3":
        secret = input(f"Password : ")


        if secret == "1122semsepiol1122":
            print("\nAKSES DITERIMA\n")
            print(f"1. Rahasia Negara\n2. Top Secret\n3. Who am i?\n4. EXIT")
            a = input(f"Pilih lah salah satu diatas : ")
            print(20*"=")

            if a == "1":
                print(f"\nSUKI SUKI DAISUKI 4LV1 AND HU TAO\n")
                input("Tekan ENTER untuk menghancurkan program...")
                break
            elif a == "2":
                print(f"\nAku Orangnya Gengsian dan Pemalu Introvet\nMasih pemula belajar python 1 bulanan\nSering Overthinking sama hal kecil\n")
                input("Tekan ENTER untuk menghancurkan program...")
                break
            elif a == "3":
                print(f"NAMA   : ANONIM\nUMUR   : ANONIM\nSTATUS : PELAJAR\n\nalasan aku bikin ini :\nkarna aku hanya ingin memasukan informasi pribadiku di script ini,mungkin hanya aku saja yang mengetahui ini kecuali orang meneliti semua codinganku\n")
                input("Tekan ENTER untuk menghancurkan program...")
                break
            else:
                print("PROGRAM HAS BEEN SHUTDOWN")
                break