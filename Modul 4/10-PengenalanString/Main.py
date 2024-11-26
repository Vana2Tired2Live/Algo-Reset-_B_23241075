# String adalah kumpulan dari karakter

data = "Ini adalah String"
print(data)
print("Panjang Karakter : ", len(data))
print("Tipe Data : ", type(data))

# 1. Cara Membuat String

"""
    1. Dengan menggunakan single quote '...'
    2. Dengan menggunakan double quote "..."
"""

data = 'Menggunakan single quote'
print(data)

data = "Menggunakan double quote"
print(data)

print("Ini adalah hari Jum'at")
print("Nama saya Ma'ruf")

# 2. Kekuatan Tanda \

# Membuat ' menjadi String
print('Mari sholat Jum\'at')
print('Saya Ma\'ruf')

# double backslash
print('C:\\user\\adam')

# tab (\t)
print("MU\t\tJuara")

# backspace (\)
print("MU\bJuara")

# newline (enter)
print("Baris satu.\nbaris dua.") #LF -> line feed # MacOS
print("Baris satu.\n\rbaris dua.") # CRLF -> Windows

# new string
print(r'C:\user\adam')

