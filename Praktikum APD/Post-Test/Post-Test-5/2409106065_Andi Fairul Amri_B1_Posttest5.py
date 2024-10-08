import os
import getpass


# Data pengguna
user = {"admin": "admin123"}
user_role = {"admin": "admin"}

# Data penghuni asrama
penghuni_asrama = []

# Registrasi pengguna baru
def daftar():
    os.system('cls || clear')
    print("Registrasi Pengguna Baru".center(50))
    print("=" * 50)
    username = input("Masukkan username: ")
    if username in user:
        print("Username sudah ada!")
        input("Klik Enter untuk melanjutkan . . .")
        return
    password = getpass.getpass("Masukkan password: ")
    user[username] = password
    user_role[username] = "pengguna"  # Semua pengguna baru adalah "pengguna"
    print("Registrasi berhasil!")
    print()
    input("Klik Enter untuk melanjutkan . . .")

# Login
def login():
    os.system('cls || clear')
    print("Login".center(50))
    print("=" * 50)
    username = input("Masukkan username: ")
    password = getpass.getpass("Masukkan password (Password akan tertutup): ")
    if user.get(username) == password:
        print("Login berhasil!")
        print()
        input("Enter untuk melanjutkan . . .")
        return username
    else:
        print("Username atau password salah!")
        print()
        input("Enter untuk melanjutkan . . .")
        return None

# Menambahkan data penghuni
def buat_data():
    os.system('cls || clear')
    print("Tambah Data Penghuni".center(50))
    print("=" * 50)
    nama = input("Nama           : ")
    universitas = input("Universitas    : ")
    tahun_masuk = input("Tahun Masuk    : ")
    nomor_hp = input("Nomor Handphone: ")
    nomor_kamar = input("Nomor Kamar    : ")
    penghuni_asrama.append([nama, universitas, tahun_masuk, nomor_hp, nomor_kamar])
    print()
    print("Data berhasil ditambahkan!")
    print()
    input("Klik Enter untuk melanjutkan . . .")

# Menampilkan data penghuni
def tampil_data():
    os.system('cls || clear')
    print("Data Penghuni Asrama".center(50))
    print("=" * 50)
    if not penghuni_asrama:
        print("Data belum tersedia.")
        print()
        input("Klik Enter untuk melanjutkan . . .")
        return
    for i, penghuni in enumerate(penghuni_asrama, start=1):
        print(f"Penghuni {i}:")
        print()
        print(f" Nama           : {penghuni[0]}")
        print(f" Universitas    : {penghuni[1]}")
        print(f" Tahun Masuk    : {penghuni[2]}")
        print(f" Nomor Handphone: {penghuni[3]}")
        print(f" Nomor Kamar    : {penghuni[4]}")
        print("=" * 50)
        print()
    input("Klik Enter untuk melanjutkan . . .")

# Memperbarui data penghuni
def ubah_data():
    tampil_data()
    print()
    print("Perbarui Data Penghuni Asrama".center(50))
    print("=" * 50)
    if not penghuni_asrama:
        return
    try:
        index = int(input("Masukkan nomor penghuni yang akan diperbarui: ")) - 1
        if 0 <= index < len(penghuni_asrama):
            nama        = input("Nama           : ")
            universitas = input("Universitas    : ")
            tahun_masuk = input("Tahun Masuk    : ")
            nomor_hp    = input("Nomor Handphone: ")
            nomor_kamar = input("Nomor Kamar    : ")
            penghuni_asrama[index] = [nama, universitas, tahun_masuk, nomor_hp, nomor_kamar]
            print("Data berhasil diperbarui!")
            input("Klik Enter untuk melanjutkan . . .")
        else:
            print("Nomor penghuni tidak valid!")
            input("Klik Enter untuk melanjutkan . . .")
    except ValueError:
        print("Input tidak valid!")
        input("Klik Enter untuk melanjutkan . . .")

# Menghapus data penghuni
def hapus_data():
    tampil_data()
    print()
    print("Hapus Data Penghuni Asrama".center(50))
    print("=" * 50)
    if not penghuni_asrama:
        return
    try:
        index = int(input("Masukkan nomor penghuni yang akan dihapus: ")) - 1
        if 0 <= index < len(penghuni_asrama):
            penghuni_asrama.pop(index)
            print()
            print("Data berhasil dihapus!")
            print()
            input("Klik Enter untuk melanjutkan . . .")
        else:
            print("Nomor penghuni tidak valid!")
            print()
            input("Klik Enter untuk melanjutkan . . .")
    except ValueError:
        print("Input tidak valid!")
        tampil_data()

# Menu utama
def main():
    while True:
        os.system('cls || clear')
        print("=" * 50)
        print("Sistem Manajemen Data Penghuni Asrama".center(50))
        print("=" * 50)
        print("1. Login")
        print("2. Daftar")
        print("3. Keluar")
        print("=" * 50)
        pilihan = input("Pilih opsi: ").strip()
        if pilihan == "1":
            username = login()
            if username:
                while True:
                    os.system('cls || clear')
                    print("=" * 50)
                    print("Sistem Manajemen Data Penghuni Asrama".center(50))
                    print("=" * 50)
                    print(f"Selamat Datang {username}, Silakan pilih menu")
                    print()
                    print("1. Tambah Data Penghuni")
                    print("2. Lihat Data Penghuni")
                    print("3. Perbarui Data Penghuni")
                    print("4. Hapus Data Penghuni")
                    print("5. Logout")
                    print("=" * 50)
                    pilihan = input("Masukkan opsi: ").strip()
                    if pilihan == "1":
                        if user_role[username] == "admin":
                            buat_data()
                        else:
                            print("Hanya admin yang dapat menambah data!")
                            print()
                            input("Klik Enter untuk melanjutkan . . .")
                    elif pilihan == "2":
                        tampil_data()
                    elif pilihan == "3":
                        if user_role[username] == "admin":
                            ubah_data()
                        else:
                            print("Hanya admin yang dapat memperbarui data!")
                            print()
                            input("Klik Enter untuk melanjutkan . . .")
                    elif pilihan == "4":
                        if user_role[username] == "admin":
                            hapus_data()
                        else:
                            print("Hanya admin yang dapat menghapus data!")
                            print()
                            input("Klik Enter untuk melanjutkan . . .")
                    elif pilihan == "5":
                        break
                    else:
                        print("Opsi tidak valid!")
                        input("Klik Enter untuk melanjutkan . . .")
        elif pilihan == "2":
            daftar()
        elif pilihan == "3":
            break
        else:
            print("Opsi tidak valid!")
            input("Klik Enter untuk melanjutkan . . .")

if __name__ == "__main__":
    main()