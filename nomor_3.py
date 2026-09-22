n_fibonacci = int(input("Masukkan berapa deret Fibonacci yang diinginkan: "))
a, b = 0, 1
for n in range (n_fibonacci):
    print(a, end=" ")
    a, b = b, a + b