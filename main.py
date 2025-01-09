import os
import CRUD as CRUD

if __name__ == "__main__":
    sistem_operasi = os.name

    match sistem_operasi:
        case "posix": os.system("clear")
        case "nt": os.system("cls")

    print("SELAMAT DATANG DI PROGRAM")
    print("  DATABASE PERPUSTAKAAN")
    print("=========================\n")

# check jika database itu ada
CRUD.init_console()

while True:
    match sistem_operasi:
        case "posix": os.system("clear")
        case "nt": os.system("cls")

    print("SELAMAT DATANG DI PROGRAM")
    print("  DATABASE PERPUSTAKAAN")
    print("=========================\n")
    
    print(f"1. Read Data")
    print(f"2. Create Data")
    print(f"3. Update Data")
    print(f"4. Delete Data")

    user_option = input("Masukkan opsi 1 - 4 : ")


    match user_option:
        case "1":
            CRUD.read_console()
        case "2":
            CRUD.create_console()
        case "3":
            CRUD.update_console()
        case "4":
            print("\tDelete Data")
        case _:
            print("masukkan pilihan yang valid!!")
            

    is_done = input("akhiri program (y/n)?")
    if is_done.lower() == "y":
        break
print("=== Program Berakhir,Terima Kasih ===")
