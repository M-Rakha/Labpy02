# Fungsi untuk menghitung harga tiket
def hitung_harga_tiket():
    # Harga tiket
    harga_reguler = 50000
    harga_vip = 100000
    diskon_member = 0.20  # Diskon 20%

    # Meminta input dari pengguna
    tipe_tiket = input("Masukkan tipe tiket (reguler/VIP): ").strip().lower()
    status_member = input("Apakah Anda memiliki kartu member? (ya/tidak): ").strip().lower()

    # Menentukan harga berdasarkan tipe tiket
    if tipe_tiket == "reguler":
        harga_tiket = harga_reguler
    elif tipe_tiket == "vip":
        harga_tiket = harga_vip
    else:
        print("Tipe tiket tidak valid!")
        return

    # Menghitung total harga dengan diskon jika berlaku
    if status_member == "ya":
        total_harga = harga_tiket * (1 - diskon_member)
    elif status_member == "tidak":
        total_harga = harga_tiket
    else:
        print("Status member tidak valid!")
        return

    # Menampilkan total harga
    print(f"Total harga yang harus dibayar: Rp{total_harga:.2f}")

# Memanggil fungsi
hitung_harga_tiket()