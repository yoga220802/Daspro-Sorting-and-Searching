# Count Sort Algorithm
# Algoritma ini bekerja dengan menghitung jumlah kemunculan setiap elemen pada list,
# lalu menggunakan informasi tersebut untuk mengurutkan data.

# List yang akan diurutkan
numbers = [64, 34, 25, 12, 22, 11, 90]

# Langkah 1: Buat array count untuk menghitung kemunculan elemen
# Ukuran array count adalah (nilai maksimum dalam list + 1)
count = [0] * (max(numbers) + 1)

# Langkah 2: Hitung jumlah kemunculan setiap elemen pada list
for k in numbers:
    count[k] += 1

# Langkah 3: Hitung jumlah kumulatif elemen di array count
# Ini menentukan posisi akhir setiap elemen di array yang diurutkan
for i in range(1, len(count)):
    count[i] += count[i - 1]

# Langkah 4: Buat array baru untuk menyimpan elemen yang sudah diurutkan
newNumbers = [0] * len(numbers)

# Langkah 5: Isi array baru berdasarkan data di array count
# Iterasi dimulai dari elemen terakhir untuk menjaga stabilitas sorting
for j in range(len(numbers) - 1, -1, -1):
    newNumbers[count[numbers[j]] - 1] = numbers[j]
    count[numbers[j]] -= 1

# Tampilkan list setelah diurutkan
print("Array Setelah Sorting:", newNumbers)

# Kompleksitas waktu:
# - O(n + k), dengan n adalah jumlah elemen dan k adalah nilai maksimum elemen.
# - Kompleksitas ruang: O(n + k) karena membutuhkan array tambahan.
