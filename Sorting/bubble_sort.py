# Bubble Sort Algorithm
# Bubble Sort bekerja dengan membandingkan dua elemen berdekatan
# dan menukar posisinya jika elemen di kiri lebih besar dari elemen di kanan.
# Proses ini dilakukan secara berulang sehingga elemen terbesar "mengapung" ke posisi akhir.

# List yang akan diurutkan
numbers = [64, 34, 25, 12, 22, 11, 90]

# Menampilkan list sebelum diurutkan
print("Bubble Sort".center(50))
print("Array Sebelum Sorting: ", numbers)

# Jumlah elemen dalam list
n = len(numbers)

# Iterasi sebanyak jumlah elemen dalam list
for i in range(n-1):  
    # Iterasi melalui elemen yang belum terurut
    for j in range(n - 1 - i):  
        # Jika elemen di kiri lebih besar dari elemen di kanan, tukar posisi
        if numbers[j] > numbers[j+1]:  
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

# Menampilkan list setelah diurutkan
print("Array Setelah Sorting: ", numbers)

# Bubble Sort memiliki kompleksitas waktu O(n^2),
# sehingga kurang efisien untuk dataset besar.