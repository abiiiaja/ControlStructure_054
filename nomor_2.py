angka_1 = int(input("Masukkan angka pertama: "))
angka_2 = int(input("Masukkan angka kedua: "))
angka_3 = int(input("Masukkan angka ketiga: "))
if angka_1 >= angka_2 and angka_1 >= angka_3:
    print(f"Angka terbesar adalah: {angka_1}")
elif angka_2 >= angka_1 and angka_1 >= angka_3:
    print(f"Angka terbesar adalah: {angka_2}")
elif angka_3 >= angka_1 and angka_3 >= angka_1:
    print(f"Angka terbesar adalah: {angka_3}")
else:
    print("Seri")
