from . import operasi


DB_NAME = "database.txt"
TEMPLATE = {
    "pk":"XXXXXX",
    "date_add":"yyyy-mm-dd",
    "judul":255* " ",
    "penulis":255* " ",
    "tahun":"yyyy"
}


def init_console():
    try:
        with open(DB_NAME,"r") as file:
            print("database tersedia,init done!")
    except:
        print("Database tidak ditemukann!!,silahkan buat database baru")
        operasi.create_first_data()
        
