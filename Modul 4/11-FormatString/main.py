# Format String
# Kata Kunci 'f' '{}'

# Contoh umum
# Tipe Data String
nama = "Ishigami Senku"
format_str = f"Selamat Datang {nama}"
print(format_str)
print(f"Selamat Datang {nama}")

# Tipe Data Boolean
bool = False
format_str = f"boolean = {bool}"
print(format_str)
print(type(bool))
print(type(format_str))

# Angka
angka = 2005.5
format_str = f"angka = {angka}"
print(format_str)

# Bilangan Bulat
angka = 10
format_str = f"Bilangan Bulat = {angka:d}"
print(format_str)

# Bilangan dengan Ordo Ribuan
angka = 2000000 # 2,000,000
format_str = f"jutaan = {angka:,}"
print(format_str)

# Bilangan Desimal
angka = 2005.54321
format_str = f'desimal = {angka:.3f}'
print(format_str)

# Menampilkan tanda + atau -
angka_minus = -10
angka_plus = +10.54321
format_minus = f'minus = {angka_minus:+d}'
format_plus = f'plus = {angka_plus:+.2f}'

print(format_minus)
print(format_plus)

# Format Persen
persentase = 0.025
format_persen = f'persen = {persentase:.25}'
print(format_persen)

# Melakukan Operasi Aritmatika
harga = 5000
jumlah = 5

format_string = f'Harga total = Rp. {harga*jumlah:,}'
print(format_string)