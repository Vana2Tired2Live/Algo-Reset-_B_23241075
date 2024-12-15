# Projek 14: Latihan Percabangan

"""
    Jika total belanja > 500rb
    Anda mendapatkan Mouse dan Keyboard
    JIka tidak, anda hanya mendapatkan Gantungan Kunci
"""

total_belanja = int(input("Masukkan Total Belanja : "))

if total_belanja >= 500000 :
    print("Selamat, anda mendapatkan hadiah Mouse dan Keyboard")
else:
    print("Belanjaan anda kurang dari Rp.500.000")
    print("Anda hanya mendapatkan Gantungan Kunci")