import os

database = []

os.system("cls")
while True:
    print(40*"=")
    pilihan = input(f"1. Program Menambahkan Judul Buku Baru\n2. Program Menghapus Buku\n3. Exit\n\npililah jawaban diatas sesuai nomor : ").strip()
    print(40*"=","\n")

    if pilihan == "1":
        os.system("cls")
        while True:
            print(f"--MENAMBAHKAN JUDUL BUKU--")
            print(29*"=")
            judul = input(f"Masukan Judul Buku : ")
            penulis = input(f"Masukan Nama Penulis : ")
            print(29*"=")

            sudah_ada = False
            for data in database:
                if data[0].lower().strip() == judul.lower().strip():
                    sudah_ada = True
                    break

            if sudah_ada:
                print("Buku Sudah ada di dalam Data")
                lanjut = input(f"apakah ingin lanjut menambahkan buku lain? (y/n) : ")
                if lanjut == "n":
                    os.system("cls")
                    break
                else:
                    os.system("cls")
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
                os.system("cls")
                break
        print("PROGRAM SELESAI")
    
    elif pilihan == "2":
        os.system("cls")
        print(f"\n--DATA BUKU--")
        if len(database):
            print(f"{'NO':<3} | {'JUDUL BUKU':<25} | {'NAMA PENULIS':<20}")
            print(50*"-")
            for index,data in enumerate(database):
                print(f"{index+1:<3} | {data[0]:<25} | {data[1]:<20}")
        else:
            os.system("cls")
            print("\nData Masih Kosong, tolong di isi dulu!\n")
            continue
        
        print(f"\nJIKA TIDAK JADI MENGHAPUS DATA KETIK HURUF APA AJA")
        hapus = input(f"Masukan No data yang ingin dihapus : ").strip()

        if hapus.isdigit():
            hapus = int(hapus)

            if 1 <= hapus <= len(database):
                buku_hapus = database.pop(hapus - 1)
                os.system("cls")
                print(f"\n--> Data Berhasil dihapus = {buku_hapus}")
            else:
                print(f"Nomor Tidak Valid!")
                continue

        else:
            os.system("cls")
            print("Batal menghapus data, kembali ke menu utama.")
            continue

    elif pilihan == "3":
        os.system("cls")
        print(f"{10*"-"}PROGRAM SELESAI{10*"-"}")
        break


    elif pilihan == "Wh1t3r0s3":
        os.system("cls")
        secret = input(f"Password : ")


        if secret == "1122semsepiol1122":
            print("\nAKSES DITERIMA\n")
            print(10*"-")
            print(f"1. Rahasia Negara\n2. Top Secret\n3. Who am i?\n4. EXIT")
            a = input(f"Pilih lah salah satu diatas : ").strip()
            print(20*"=")

            if a == "1":
                print(f"\nSUKI SUKI DAISUKI 4LV1 AND HU TAO\n")
                input("Tekan ENTER untuk menghancurkan program...")
                os.system("cls")
                break
            elif a == "2":
                print(f"\nAku Orangnya Gengsian dan Pemalu Introvet\nMasih pemula belajar python 1 bulanan\nSering Overthinking sama hal kecil\n")
                input("Tekan ENTER untuk menghancurkan program...")
                os.system("cls")
                break
            elif a == "3":
                print(f"NAMA   : ANONIM\nUMUR   : ANONIM\nSTATUS : PELAJAR\n\nalasan aku bikin ini :\nkarna aku hanya ingin memasukan informasi pribadiku di script ini,mungkin hanya aku saja yang mengetahui ini kecuali orang meneliti semua codinganku\n")
                input("Tekan ENTER untuk menghancurkan program...")
                os.system("cls")
                break
            else:
                print("PROGRAM HAS BEEN SHUTDOWN")
                os.system("cls")
                break
