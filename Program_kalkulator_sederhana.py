# Program Matematika Menggunakan Def
import os

def header():
    print(40*"-")
    print(f"{'PROGRAM MATEMATIKA':^40}")
    print(40*"-")

def user_input():
    angka1 = int(input(f"Masukan Angka ke-1: "))
    angka2 = int(input(f"Masukan Angka ke-2: "))
    return angka1,angka2

def pertambah(angka1,angka2):
    return angka1 + angka2

def perkurang(angka1,angka2):
    return angka1 - angka2

def perkalian(angka1,angka2):
    return angka1 * angka2

def pembagian(angka1,angka2):
    return angka1 / angka2

def display(message,hasil):
    print(f"hasil dari {message} = {hasil}")
    return message,hasil

while True:
    os.system('cls')
    header()
    try:
        angka1,angka2 = user_input()
    except:
        os.system("cls")
        print(f"Program Tidak boleh kosong/huruf, hanya angka! LOL")
        input(f"press enter to continue...")
        continue
    try:
        pilihan = int(input(f"\n1. Pertambahan\n2. Perkurangan\n3. Perkalian\n4. Pembagian\n\nMasukan Nomor sesuai diatas yang anda inginkan: "))
    except:
        os.system('cls')
        print(f"\n1. Pertambahan\n2. Perkurangan\n3. Perkalian\n4. Pembagian\n")
        print(f"lu salah ketik ya bro?\nNilai Tidak Valid! Masukan Angka sesuai dengan pilihan diatas! \ncontoh: 1")
        input(f"press enter to continue...")
        continue

    if pilihan == 1:
        message = "Pertambahan"
        hasil = pertambah(angka1,angka2)
    elif pilihan == 2:
        message = "Perkurangan"
        hasil = perkurang(angka1,angka2)
    elif pilihan == 3:
        message = "Perkalian"
        hasil = perkalian(angka1,angka2)
    elif pilihan == 4:
        message = "Pembagian"
        try:
            hasil = pembagian(angka1,angka2)
        except:
            print(f"Pembagian tidak bisa menggunakan angka 0!")
            input(f"press enter to continue...")
            continue
    else:
        os.system('cls')
        print(f"Nilai Tidak Valid! Masukan Angka sesuai dengan pilihan diatas! \ncontoh: 1")
        input(f"press enter to continue...")
        continue

    display(message,hasil)

    selesai = input(f"Ingin Menghitung lagi? (y/n): ")
    if selesai == "n":
        print(f"Program Selesai!")
        break
    else:
        continue
