# Latihan (Pengecek Nilai)
"""
    Jika nilai >90, nilai huruf = A
        nilai 85 - 90, nilai huruf = A-
        nilai 80 - 85, nilai huruf = B+
        nilai 75 - 79, nilai huruf = B
        nilai 70 - 74, nilai huruf = B-
        nilai 65 - 69, nilai huruf = C+
        nilai 60 - 64, nilai huruf = C
        nilai 55 - 59, nilai huruf = D
        nilai <55, nilai huruf = E
"""
nilai = int(input("Masukkan Nilai : "))

if nilai >= 90 :
    print("Nilai anda A, selamat!")
elif nilai >= 85 and 90 :
    print("Nilai anda A-")
elif nilai >= 80 and 85 :
    print("Nilai anda B+")
elif nilai >= 75 and 79 :
    print("Nilai anda B")
elif nilai >= 70 and 74 :
    print("Nilai anda B-")
elif nilai >= 65 and 69 :
    print("Nilai anda C-")
elif nilai >= 60 and 64 :
    print("Nilai anda C")
elif nilai >= 55 and 59 :
    print("Nilai anda D")
else:
    print("Nilai anda E, coba lagi lain waktu...")