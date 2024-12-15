# Latihan (Diskon Membership)
"""
    Jika Pelanggan memiliki kartu Member dan belanja diatas 500rb, maka dapat diskon 20%,
    namun jika kurang dari 500rb maka dapat diskon 10%
    
    Tetapi jika pelanggan tidak memiliki kartu Member dan belanja diatas 500rb, maka dapat diskon 5%
    namun jika kurang dari 500rb maka tidak dapat diskon
    
    Hasil Program:
    Apakah Member? (ya/tidak) : ya
    Masukkan Total Belanja : Rp.550.000
    output:
        Total Belanja : Rp.550.000
        Diskon persen : 20%
        Potongan Harga : Rp.110.000
        Bayar : Rp.440.000
"""
def hitung_diskon():
    # Input dari user
    member = input("Apakah Anda Member? (ya/tidak) : ").strip().lower()
    total_belanja = float(input("Masukkan Total Belanja : Rp."))

    # Inisialisasi variabel
    diskon_persen = 0

    # Logika diskon berdasarkan member dan total belanja
    if member == "ya":
        if total_belanja > 500000:
            diskon_persen = 20
        else:
            diskon_persen = 10
    elif member == "tidak":
        if total_belanja > 500000:
            diskon_persen = 5

    # Perhitungan
    potongan_harga = total_belanja * (diskon_persen / 100)
    total_bayar = total_belanja - potongan_harga

    # Output
    print(f"Total Belanja : Rp.{total_belanja:,.0f}")
    print(f"Diskon persen : {diskon_persen}%")
    print(f"Potongan Harga : Rp.{potongan_harga:,.0f}")
    print(f"Bayar : Rp.{total_bayar:,.0f}")

# Jalankan program
hitung_diskon()

