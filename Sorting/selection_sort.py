# Selection Sort Algorithm
# Algoritma ini bekerja dengan mencari elemen terkecil pada list yang belum terurut,
# lalu menukarnya dengan elemen pertama dari bagian tersebut.

# List yang akan diurutkan
numbers = [64, 34, 25, 12, 22, 11, 90]

# Menampilkan list sebelum diurutkan
print("Selection Sort".center(50))
print("Array Sebelum Sorting: ", numbers)

# Jumlah elemen dalam list
n = len(numbers)

# Iterasi sebanyak jumlah elemen dalam list
for i in range(n-1):
    # Tentukan index elemen terkecil pada list yang belum terurut
    min_index = i
    # Cari elemen terkecil pada bagian list yang belum terurut
    for j in range(i+1, n):
        # Jika elemen pada index j lebih kecil, perbarui min_index
        if numbers[j] < numbers[min_index]:
            min_index = j
    # Tukar elemen terkecil dengan elemen pertama pada bagian yang belum terurut
    numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

# Menampilkan list setelah diurutkan
print("Array Setelah Sorting: ", numbers)

# Selection Sort memiliki kompleksitas waktu:
# - Kasus Terburuk: O(n^2)
# - Kasus Terbaik: O(n^2) (meskipun list sudah terurut).
# - Rata-rata: O(n^2)
# Algoritma ini menggunakan kompleksitas ruang O(1).
