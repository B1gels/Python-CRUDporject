from . import operasi

def read_console():
    data_file = operasi.read()
    Index = "NO"
    judul = "Judul"
    penulis = "Penulis"
    tahun = "Tahun"


    # HEADER
    print("\n"+"="*100)
    print(f"{Index:4} | {judul:40} | {penulis:40} | {tahun:5}")
    print("-"*100)

    # DATA
    for Index,data in enumerate(data_file):
        data_break = data.split(",")
        pk = data_break[0]
        date_add = data_break[1]
        penulis = data_break[2]
        judul = data_break[3]
        tahun = data_break[4]
        print(f"{Index+1:4} | {judul:.40} | {penulis:.40} | {tahun:4}",end="")

    # FOOTER
    print("="*100+"\n")

def create_console():
    print("\n\n"+"="*100)
    print("SILAHKAN TAMBAH DATA BUKU\n")
    penulis = input("penulis\t: ")
    judul = input("judul\t: ")
    while True:
        try:
            tahun = int(input("Tahun\t: "))
            if len(str(tahun)) == 4:
                break
            else:
                print("Tahun tidak valid!! (yyyy)")

        except:
            print("masukkan angka!!")
    operasi.create(tahun,judul,penulis)
    print("\nBERIKUT ADALAH DATA BARU ANDA")
    read_console()


def update_console():
    read_console()
    while True:
        print("Silahkan pilih nomor yang ingin diUpdate:")
        no_buku = int(input("Nomor Buku\t: "))
        data_buku = operasi.read(index=no_buku)

        if data_buku:
            break
        else:
            print("nomor tidak valid,silahkan masukkan lagi")

    data_break = data_buku.split(",")
    pk = data_break[0]
    data_add = data_break[1]
    penulis = data_break[2]
    judul = data_break[3]
    tahun = data_break[4][:-1]

    while True:
        print("\n"+"="*100)
        print("Silahkan pilih data yang ingin diubah")
        print(f"1.Judul  \t: {judul:.40}")
        print(f"2.penulis\t: {penulis:.40}")
        print(f"3.tahun  \t: {tahun:4}")

        user_option = input("pilih data [1,2,3] : ")
        print("\n"+"="*100)
        match user_option:
            case "1": judul     = input("judul\t: ")
            case "2": penulis   = input("penulis\t: ")
            case "3": 
                while True:
                    try:
                        tahun = int(input("Tahun\t: "))
                        if len(str(tahun)) == 4:
                            break
                        else:
                            print("Tahun tidak valid!! (yyyy)")

                    except:
                        print("masukkan angka!!")
            case _:
                print("index yang dimasukkan tidak cocok :(")

        print("Data baru anda")
        print(f"1. Judul\t: {judul:.40}")
        print(f"2. Penulis\t: {penulis:.40}")
        print(f"3. Tahun\t: {tahun:4}")
        is_done = input("apakah selesai update?[y/n] : ")
        if is_done == "y" or is_done == "Y":
            break
    
    operasi.update(no_buku,pk,data_add,judul,penulis,tahun)


def delete_console():
    print("ini delete Console")