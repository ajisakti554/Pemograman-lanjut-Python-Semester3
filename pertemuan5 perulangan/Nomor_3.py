# Versi 1: Menggunakan perulangan for
def lirik_anak_ayam_for(n):
    print("\n=== Versi For ===")
    print(f"Anak ayam turunlah {n}")
    
    for i in range(n-1, 0, -1):
        print(f"Mati satu tinggallah {i}")
    
    print("Mati satu tinggal induknya")

# Versi 2: Menggunakan while
def lirik_anak_ayam_while(n):
    print("\n=== Versi While ===")
    print(f"Anak ayam turunlah {n}")
    
    sisa = n
    while sisa > 1:
        sisa -= 1
        print(f"Mati satu tinggallah {sisa}")
    
    print("Mati satu tinggal induknya")

# Versi 3: Menggunakan while dengan counter
def lirik_anak_ayam_while_counter(n):
    print("\n=== Versi While dengan Counter ===")
    print(f"Anak ayam turunlah {n}")
    
    counter = 1
    sisa = n
    while counter <= n-1:
        sisa = n - counter
        print(f"Mati satu tinggallah {sisa}")
        counter += 1
    
    print("Mati satu tinggal induknya")

# Input dari pengguna
n = int(input("Masukkan jumlah anak ayam (N): "))

# Memastikan N > 0
if n > 0:
    # Menjalankan ketiga versi program
    lirik_anak_ayam_for(n)
    lirik_anak_ayam_while(n)
    lirik_anak_ayam_while_counter(n)
else:
    print("N harus lebih besar dari 0")