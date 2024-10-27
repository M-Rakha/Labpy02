Nama : MUHAMMAD RAKHA GHANI
Kelas : TI.24.A3
NIM : 312410421
Matkul : Bahasa Pemrograman

# Latihan 3

# Program Tiket Bioskop

![gambar](https://github.com/M-Rakha/Labpy02/blob/246ae1a66dbe1dd99ac193dcc564239d882a7d9c/images/latihan3.png)

```python
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
```

Program ini akan menentukan harga pesanan tiket bioskop, Yang reguler/Vip, dan jika Vip harga 100.000, dan jika reguler 80.0000, dan jika memiliki kartu member pelanggan tersebut akan mendapatkan diskon 20%

``` python
 harga_reguler = 50000
    harga_vip = 100000
```

Untuk menentukan harga tiket tersebut

``` python
tipe_tiket = input("Masukkan tipe tiket (reguler/VIP): ").strip().lower()
    status_member = input("Apakah Anda memiliki kartu member? (ya/tidak): ").strip().lower()
```

Pengguna diminta untuk memasukkan tipe tiket yang mereka inginkan, bisa "reguler" atau "VIP", Pengguna juga diminta untuk menjawab apakah mereka memiliki kartu member, dengan pilihan "ya" atau "tidak"

``` python
if tipe_tiket == "reguler":
        harga_tiket = harga_reguler
    elif tipe_tiket == "vip":
        harga_tiket = harga_vip
    else:
        print("Tipe tiket tidak valid!")
        return
```

Jika tipe tiket adalah "reguler", harga tiket akan diatur menjadi harga_reguler (Rp50.000), Jika tipe tiket adalah "VIP", harga tiket akan diatur menjadi harga_vip (Rp100.000), Jika tipe tiket yang dimasukkan tidak valid, fungsi akan menampilkan pesan error dan menghentikan proses

``` python
if status_member == "ya":
        total_harga = harga_tiket * (1 - diskon_member)
    elif status_member == "tidak":
        total_harga = harga_tiket
    else:
        print("Status member tidak valid!")
        return
```

Jika pengguna adalah member (status_member == "ya"), harga tiket akan dikurangi diskon 20%, Jika pengguna bukan member (status_member == "tidak"), harga tiket tetap sama tanpa pengurangan, Jika input untuk status member tidak valid, misalnya selain "ya" atau "tidak", fungsi akan menampilkan pesan error dan menghentikan eksekusi

``` python
print(f"Total harga yang harus dibayar: Rp{total_harga:.2f}")
```

Setelah menghitung total harga, anda dapat langsung menjalankan fungsinya

Hasil program tersebut:

![gambar](https://github.com/M-Rakha/Labpy02/blob/a77cfa90288be7ef4a88ebb19d35814b35bec02a/images/python1.png)

Code program tersebut:

![gambar](https://github.com/M-Rakha/Labpy02/blob/45b616bb66fc07eddf7f961d59deaaf373be11a9/images/python2.png)

Dan ini flowchart nya

![gambar](https://github.com/andreanbadeh/Labpy02/raw/6478a017cad461f2f5d5a1b6931d4ac7004497dd/Image/tiket%20biskop.png)

# Prorgam Kalkulator Sederhana

![gambar](https://github.com/M-Rakha/Labpy02/blob/0d565d11da97c7c10143e497bcc05fc40fcf8ad6/images/kalkulator.png)

``` python
# Fungsi untuk kalkulator sederhana
def kalkulator():
    # Meminta input dari pengguna
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))
    operator = input("Masukkan operator (+, -, *, /): ").strip()

    # Menghitung hasil berdasarkan operator yang dipilih
    if operator == "+":
        hasil = angka1 + angka2
    elif operator == "-":
        hasil = angka1 - angka2
    elif operator == "*":
        hasil = angka1 * angka2
    elif operator == "/":
        if angka2 != 0:
            hasil = angka1 / angka2
        else:
            print("Error: Pembagian dengan nol tidak diperbolehkan!")
            return
    else:
        print("Error: Operator tidak valid!")
        return

    # Menampilkan hasil
    print(f"Hasil: {hasil}")

# Memanggil fungsi
kalkulator()
```

Program kalkulator sederhana dalam Python adalah proyek yang baik untuk pemula dan programmer tingkat lanjut. Program ini memungkinkan pengguna untuk melakukan operasi matematika seperti penjumlahan, pengurangan, perkalian, dan pembagian.

``` pygthon
angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))
    operator = input("Masukkan operator (+, -, *, /): ").strip()
```


