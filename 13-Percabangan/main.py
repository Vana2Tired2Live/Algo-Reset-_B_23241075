# Percabangan
# Struktur
"""
    1. if-ny
    2. Punya Kondisi
    3. Punya aksi
"""    
nama = input("Masukkan nama : ")

# Percabangan yang In line (Satu baris)
if nama == "Okarun" : print("Selamat Datang")
print("Terima kasih")

# Percabangan Indentasi
if nama == "Okarun" :
    print("Selamat Datang")
    print("Selamat Belajar Python")
print("Bukan Bagian Percabangan")

# Percabangan 1 kondisi 2 aksi
# Menggunakan kata kunci "else"

if nama == "Okarun" :
    print("Selamat Datang")
else:
    print(f"Anda {nama}, bukan Okarun")
print("Terima kasih")