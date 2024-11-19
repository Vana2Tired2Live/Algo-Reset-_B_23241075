# Operasi Komparasi

# Setiap hasil komparasi selalu bertipe Boolean (TRUE/FALSE)

# >, <, =, !=, >=, <=, is, dan is not

# Deklarasi Variabel
a = 4
b = 2

# Lebih besar dari (>)
print("=== Lebih besar dari (>) ===")
hasil = a > 2 #TRUE
print(a, ">", 2, "=", hasil)
hasil = b > 3 #FALSE
print(b, ">", 3, "=", hasil)
hasil = b > 2 #FALSE
print(b, ">", 2, "=", hasil)

# Kurang dari (<)
print("=== Kurang dari (<) ===")
hasil = a < 2 #FALSE
print(a, "<", 2, "=", hasil)
hasil = b < 3 #TRUE
print(b, "<", 3, "=", hasil)
hasil = b < 2 #FALSE
print(b, "<", 2, "=", hasil)

# Lebih dari Sama Dengan (>=)
print("=== Lebih dari Sama Dengan (>=) ===")
hasil = a >= 2 #TRUE
print(a, ">=", 2, "=", hasil)
hasil = b >= 3 #FALSE
print(b, ">=", 3, "=", hasil)
hasil = b >= 2 #TRUE
print(b, ">=", 2, "=", hasil)

# Kurang dari Sama Dengan (<=)
print("=== Kurang dari Sama Dengan (<=) ===")
hasil = a <= 2 #FALSE
print(a, "<=", 2, "=", hasil)
hasil = b <= 3 #TRUE
print(b, "<=", 3, "=", hasil)
hasil = b <= 2 #TRUE
print(b, "<=", 2, "=", hasil)

# Sama Dengan (==)
print("=== Sama Dengan (==) ===")
hasil = a == 2 #FALSE
print(a, "==", 2, "=", hasil)
hasil = b == 3 #FALSE
print(b, "==", 3, "=", hasil)
hasil = b == 2 #TRUE
print(b, "==", 2, "=", hasil)

# Tidak Sama Dengan (!=)
print("=== Tidak Sama Dengan (!=) ===")
hasil = a != 2 #TRUE
print(a, "!=", 2, "=", hasil)
hasil = b != 2 #FALSE
print(b, "!=", 2, "=", hasil)

# is adalah komparasi Objek
x = 5
y = 5
hasil = x is y
print("Nilai x : ", x, "id: ", hex(id(x)))
print("Nilai y : ", y, "id: ", hex(id(y)))
print(x, "is", y, "=", hasil)

# is not adalah komparasi Objek
x = 5
y = 5
hasil = x is not y
print("Nilai x : ", x, "id: ", hex(id(x)))
print("Nilai y : ", y, "id: ", hex(id(y)))
print(x, "is not", y, "=", hasil)