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