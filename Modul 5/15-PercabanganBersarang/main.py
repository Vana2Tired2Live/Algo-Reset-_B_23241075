# Percabangan Bersarang / Nested IF

# Kalkulator
# +, -, x, /, mod, //, pangkat(exponen)

print(20*"=")
print("Kalkulator Sederhana")
print(20*"=")

angka_1 = float(input("Masukkan Bilangan 1 : "))
operator = input("Operator (+,-,x,/,%,//,**) = ")
angka_2 = float(input("Masukkan Bilangan 2 : "))

# Percabangan Bersarang (ELIF Bersarang)

if operator == '+' :
    hasil = angka_1 + angka_2
    print(f"Hasilnya adalah = {hasil}")
elif operator == '-' :
    hasil = angka_1 - angka_2
    print(f"Hasilnya adalah = {hasil}")
elif operator == 'x' :
    hasil = angka_1 * angka_2
    print(f"Hasilnya adalah = {hasil}")
elif operator == '/' :
    hasil = angka_1 / angka_2
    print(f"Hasilnya adalah = {hasil}")
elif operator == '%' or operator == 'mod':
    hasil = angka_1 % angka_2
    print(f"Hasilnya adalah = {hasil}")
elif operator == '//' :
    hasil = angka_1 // angka_2
    print(f"Hasilnya adalah = {hasil}")
elif operator == '**' :
    hasil = angka_1 ** angka_2
    print(f"Hasilnya adalah = {hasil}")
else:
    print(f"Operator {operator} tidak ditemukan")

