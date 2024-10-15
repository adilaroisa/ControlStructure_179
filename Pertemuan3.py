# 1. Write a PYTHON program to evaluate the student performance
def evaluate_performance(percentage):
    if percentage >= 90:
        return "Excellent performance" #  Kondisi if jika nilai percentage lebih besar atau sama dengan 90, maka program mencetak "Excellent performance".
    elif percentage >= 80:
        return "Very Good performance" # Kondisi elif Memeriksa apakah percentage memenuhi kondisi yang lebih rendah(lebih bessar sama dengan 80)
    elif percentage >= 70:
        return "Good performance" # Kondisi elif Memeriksa apakah percentage memenuhi kondisi yang lebih rendah(lebih bessar sama dengan 70)
    elif percentage >= 60:
        return "Average performance" # Kondisi elif Memeriksa apakah percentage memenuhi kondisi yang lebih rendah(lebih bessar sama dengan 60)
    else:
        return "Below average performance" # Jika nilai tidak memenuhi kondisi sebelumnya, maka program akan mencetak "Bwloe average performsnce".

percentage = int(input("Enter the student's percentage: ")) # Digunakan untuk meminta user memasukkan nilai persentase 
print(evaluate_performance(percentage))


# 2. Write a PYTHON program to find largest of three numbers!
def largest_of_three(no1, no2, no3): 
    if no1 >= no2 and no1 >= no3: # Kondisi if Memeriksa apakah no1 lebih besar atau sama dengan no2 dan no3.
        return no1
    elif no2 >= no1 and no2 >= no3: # Kondisi elif Memeriksa apakah no2 lebih besar atau sama dengan no1 dan no3.
        return no2
    else:                #  kondisi else Jika kondisi sebelumnya tidak terpenuhi, maka no3 adalah angka terbesar.
        return no3 

no1 = int(input("Enter first number: ")) # Meminta user memasukkan tiga angka
no2 = int(input("Enter second number: "))
no3 = int(input("Enter third number: "))
print("The largest number is:", largest_of_three(no1, no2, no3))


# 3. Write a PYTHON program to print Fibonacci series up to n!
def fibonacci_series(n):
    a, b = 0, 1           # Variabel a dan b diatur dengan nilai 0 dan 1, dua angka pertama dalam deret Fibonacci
    fib_sequence = []
    while a <= n:         # Menjalankan loop sampai jumlah angka yang dicetak mencapai n
        fib_sequence.append(a)
        a, b = b, a + b   # Menggeser nilai a dan b ke angka Fibonacci berikutnya
    return fib_sequence

n = int(input("Enter the value of n: ")) #  Digunakan untuk meminta jumlah angka Fibonacci yang akan dicetak
print("Fibonacci series up to", n, "is:", fibonacci_series(n))


# 4. Write a PYTHON program to print odd numbers up to n!
def odd_numbers_up_to(n):
    odd_numbers = [i for i in range(1, n + 1) if i % 2 != 0] # Loop for mengulangi nilai i dari 1 hingga n.
    # if i % 2 != 0: Memeriksa apakah i adalah bilangan ganjil dengan memeriksa sisa pembagian i dengan 2. Jika hasilnya tidak sama dengan 0, i adalah bilangan ganjil
    return odd_numbers

n = int(input("Enter the value of n: "))  # Digunakan untuk meminta batas atas n yang akan menjadi batas akhir dari bilangan ganjil yang dicetak
print("Odd numbers up to", n, "are:", odd_numbers_up_to(n))


# 5. Write a PYTHON program to produce following design
def print_pattern(n):
    for i in range(1, n + 1):  # loop for yang mengulangi nilai i mulai dari 1 hingga n. range(1, n + 1) menghasilkan angka dari 1 hingga n
        print(" ".join([str(i)] * i)) # str(i) mengubah nilai i menjadi string. 
    # Metode join digunakan untuk menggabungkan elemen-elemen dalam daftar menjadi satu string, dengan pemisah berupa spasi

n = int(input("Enter the value of n: "))  # Digunakan untuk mendapatkan nilai n dari pengguna, yang menentukan jumlah baris dalam pola segitiga
print_pattern(n)
