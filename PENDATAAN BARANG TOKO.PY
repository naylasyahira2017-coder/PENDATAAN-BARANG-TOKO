nama_toko = "TOKO FALAH ENTERPRISE"

barang_list = [
    {"nama": "Mie Instan", "harga": 3000, "stok": 20},
    {"nama": "Gula", "harga": 12000, "stok": 10},
    {"nama": "Beras", "harga": 50000, "stok": 5},
    {"nama": "Teh Celup", "harga": 7000, "stok": 15},
]

def tampilkan_barang():
    print(f"\n=== DATA BARANG {nama_toko} ===")
    print("| No | NAMA BARANG | HARGA | STOK |")
    print("-" * 35)
    
    if len(barang_list) == 0:
        print("Belum ada data barang")
        return
    
    for i, barang in enumerate(barang_list, start=1):
        print(f"| {i:<2} | {barang['nama']:<10} | Rp{barang['harga']:<6} | {barang['stok']:<4} |")
    print("-" * 35)

def tambah_barang():
    print("\n=== TAMBAH BARANG ===")
    
    nama = input("Nama barang : ")
    
    while True:
        harga_input = input("Harga : ")
        if harga_input.isdigit():
            harga = int(harga_input)
            break
        else:
            print("Harga harus berupa angka!")
    
    while True:
        stok_input = input("Stok : ")
        if stok_input.isdigit():
            stok = int(stok_input)
            break
        else:
            print("Stok harus berupa angka!")
    
    barang_list.append({"nama": nama, "harga": harga, "stok": stok})
    print("Barang berhasil ditambahkan!")

def edit_barang():
    if len(barang_list) == 0:
        print("\nBelum ada data barang")
        return
    
    tampilkan_barang()
    
    while True:
        kode_input = input("\nMasukkan nomor barang yang ingin diedit: ")
        if kode_input.isdigit():
            kode = int(kode_input)
            break
        else:
            print("Input harus berupa angka!")
    
    if 1 <= kode <= len(barang_list):
        print("Kosongkan jika tidak ingin mengubah")
        
        nama_baru = input("Nama baru : ")
        if nama_baru != "":
            barang_list[kode-1]['nama'] = nama_baru
        
        harga_baru = input("Harga baru: ")
        if harga_baru != "" and harga_baru.isdigit():
            barang_list[kode-1]['harga'] = int(harga_baru)
        
        stok_baru = input("Stok baru : ")
        if stok_baru != "" and stok_baru.isdigit():
            barang_list[kode-1]['stok'] = int(stok_baru)
        
        print("Data barang berhasil diubah!")
    else:
        print("Nomor tidak valid!")

def hapus_barang():
    if len(barang_list) == 0:
        print("\nBelum ada data barang")
        return
    
    tampilkan_barang()
    
    while True:
        kode_input = input("\nMasukkan nomor barang yang ingin dihapus: ")
        if kode_input.isdigit():
            kode = int(kode_input)
            break
        else:
            print("Input harus berupa angka!")
    
    if 1 <= kode <= len(barang_list):
        barang_list.pop(kode-1)
        print("Barang berhasil dihapus!")
    else:
        print("Nomor tidak valid!")

def cari_barang():
    print("\n=== CARI BARANG ===")
    
    if len(barang_list) == 0:
        print("Belum ada data barang")
        return
    
    cari = input("Cari nama barang: ")
    
    hasil = []
    for barang in barang_list:
        if cari.lower() in barang['nama'].lower():
            hasil.append(barang)
    
    if len(hasil) > 0:
        print(f"\nDitemukan {len(hasil)} barang:")
        print("| No | NAMA BARANG | HARGA | STOK |")
        print("-" * 35)
        for i, barang in enumerate(hasil, start=1):
            print(f"| {i:<2} | {barang['nama']:<10} | Rp{barang['harga']:<6} | {barang['stok']:<4} |")
        print("-" * 35)
    else:
        print("Barang tidak ditemukan")

def menu():
    while True:
        print(f"\n===== SISTEM PENDATAAN {nama_toko} =====")
        print("1. Tampilkan Barang")
        print("2. Tambah Barang")
        print("3. Edit Barang")
        print("4. Hapus Barang")
        print("5. Cari Barang")
        print("0. Keluar")
        
        pilih = input("Pilih menu: ")
        
        if pilih == "1":
            tampilkan_barang()
        elif pilih == "2":
            tambah_barang()
        elif pilih == "3":
            edit_barang()
        elif pilih == "4":
            hapus_barang()
        elif pilih == "5":
            cari_barang()
        elif pilih == "0":
            print("\nTerima kasih! Program selesai.")
            break
        else:
            print("Menu tidak valid! Pilih 0-5")

if __name__ == "__main__":
    menu()
