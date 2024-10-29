# Memasukkan input suhu dalam Fahrenheit dari User
fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))

# Rumus konversi Fahrenheit ke Celsius
celsius = (fahrenheit - 32) * 5/9

# Hasil konversi
print(f"Suhu dalam Celsius: {celsius:.2f}°C")
