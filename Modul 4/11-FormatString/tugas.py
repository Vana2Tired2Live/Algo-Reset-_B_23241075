# Program Menghitung BMI

tinggi_cm = float(input("Masukkan tinggi badan Anda (dalam cm): "))
berat_kg = float(input("Masukkan berat badan Anda (dalam kg): "))

# Konversi tinggi dari cm ke meter
tinggi_m = tinggi_cm / 100

# Perhitungan BMI
bmi = berat_kg / (tinggi_m ** 2)
print(f"Skor BMI anda adalah: {bmi:.1f}")
