from . import Database
import time
from .util import random_string
import os

# *fungsi yang akan membuat file ketika file belum ada
def create_first_data():
    penulis = input("penulis: ")
    judul = input("judul: ")
    while True:
        try:
            tahun = int(input("Tahun\t: "))
            if len(str(tahun)) == 4:
                break
            else:
                print("Tahun tidak valid!! (yyyy)")

        except:
            print("masukkan angka!!")

    data = Database.TEMPLATE.copy()

    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H:%M:%S%z",time.gmtime())
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun)

    data_str= f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'
    print(data_str)
    try:
        with open(Database.DB_NAME,"w",encoding="utf-8") as file:
            file.write(data_str)
    except: 
        print("penambahan gagal,Mulai ulang program!!!")
    

# *Fungsi untuk membaca semua buku yang ada di dalam file,dan menampilkannya
def read(**kwargs):
    try:
        with open(Database.DB_NAME,"r") as file:
            content = file.readlines()
            jumlah_buku = len(content)
            if "index" in kwargs:
                index_buku = kwargs["index"]-1
                if index_buku < 0 or index_buku > jumlah_buku:
                    return False
                else:
                    return content[index_buku]
            else:
                return content
    except:
        print("error membaca database!!")
        return False
    

# *fungsi untuk membuat buku baru (judul,penulis,tahun)
def create(tahun,judul,penulis):
    data = Database.TEMPLATE.copy()

    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H:%M:%S%z",time.gmtime())
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun)

    data_str= f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'
    try:
        with open(Database.DB_NAME,"a",encoding="utf-8") as file:
            file.write(data_str)
    except: 
        print("penambahan gagal,Mulai ulang program!!!")


# *fungsi untuk mengubah nilai (penulis ,judul,tahun)
def update(no_buku,pk,data_add,judul,penulis,tahun):
    data = Database.TEMPLATE.copy()

    data["pk"] = pk
    data["date_add"] = data_add
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun)

    data_str= f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'
    panjang_data = len(data_str)
    
    try:
        with open(Database.DB_NAME,"r+",encoding="utf-8") as file:
            file.seek(panjang_data*(no_buku-1))
            print(file.tell())
            file.write(data_str)
    except Exception as error:
        print("error mengupdate database!!!")
        print(f"ERROR : {error}")


# *fungsi untuk menghapus buku
def delete(no_buku):
    try:
        with open(Database.DB_NAME,"r") as file:
            counter = 0
            while(True):
                content = file.readline()
                if len(content) == 0:
                    break
                elif counter == no_buku - 1:
                    pass
                else:
                    with open("data-temp.txt","a",encoding="utf-8") as temporary_file:
                        temporary_file.write(content)
                counter += 1
    except:
        print("error gagal menghapus buku !!!")

    os.replace("data-temp.txt",Database.DB_NAME)