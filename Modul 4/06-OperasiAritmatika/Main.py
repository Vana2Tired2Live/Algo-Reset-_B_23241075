# Operasi Aritmatika

# Variabel dengan nilai Awal
a = 10
b = 3

# Operasi Penjumlahan (+)
hasil = a + b
print(a, "+", b, "=", hasil)

# Operasi Pengurangan (-)
hasil = a - b
print(a, "-", b, "=", hasil)

# Operasi Perkalian (*)
hasil = a * b
print(a, "*", b, "=", hasil)

# Operasi Pembagian (/)
hasil = a / b
print(a, "/", b, "=", hasil)

# Operasi Pemangkatan (**)
hasil = a ** b
print(a, "**", b, "=", hasil)

# Operasi Modulus (%)
hasil = a % b
print(a, "%", b, "=", hasil)

# Operasi Floor Division (//)
hasil = a // b
print(a, "//", b, "=", hasil)

# Prioritas Operasi

# 1. ()
# 2. Perkalian, Pembagian, dll => *, /, **, //
# 3. Penjumlahan dan Pengurangan

x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print(x, "**", y, "*", z, "+", x, "/", y, "-", y, "%", z, "//", x, "=", hasil)
