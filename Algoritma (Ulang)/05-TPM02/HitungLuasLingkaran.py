import math

# Memasukkan input jari-jari lingkaran dari User
jari_jari = float(input("Masukkan jari-jari lingkaran: "))

# Rumus menghitung luas lingkaran
luas = math.pi * (jari_jari ** 2)

# Menampilkan hasil perhitungan
print(f"Luas lingkaran dengan jari-jari {jari_jari} adalah {luas:.2f}")
