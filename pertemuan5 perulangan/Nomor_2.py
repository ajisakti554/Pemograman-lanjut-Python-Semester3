# Program menghitung jumlah kelipatan 5

def hitung_kelipatan_lima(n):
    # Inisialisasi variabel untuk menyimpan jumlah
    jumlah = 0
    # List untuk menyimpan bilangan kelipatan 5
    kelipatan = []
    
    
    # Mencari kelipatan 5
    for i in range(1, n + 1):
        if i % 5 == 0:
            kelipatan.append(i)
            jumlah += i
    
    # Output hasil
    if len(kelipatan) == 0:
        print(f"Input N: {n}")
        print(f"Output: 0")
        print("Keterangan: Tidak ada bilangan kelipatan 5 antara 1 s.d.", n)
    else:
        print(f"Input N: {n}")
        print(f"Output: {jumlah}")
        print("Keterangan: Bilangan kelipatan 5 antara 1 s.d.", n, "adalah", end=" ")
        print(*kelipatan, sep=", ")
        if len(kelipatan) > 1:
            print(f"{' + '.join(map(str, kelipatan))} = {jumlah}")

# Input dari pengguna
n = int(input("Masukkan nilai N: "))

# Memanggil fungsi
hitung_kelipatan_lima(n)