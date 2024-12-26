# Insertion Sort Algorithm
# Insertion Sort menyerupai cara seseorang menyusun kartu di tangan.
# Elemen dari array ditempatkan pada posisi yang benar secara bertahap.

# List yang akan diurutkan
numbers = [64, 34, 25, 12, 22, 11, 90]

# Menampilkan list sebelum diurutkan
print("Insertion Sort".center(50))
print("Array Sebelum Sorting: ", numbers)

# Jumlah elemen dalam list
n = len(numbers)

# Iterasi dimulai dari elemen kedua hingga elemen terakhir
for i in range(1, n):  
    # Simpan elemen yang akan diurutkan ke dalam variabel key
    key = numbers[i]  
    # Simpan index elemen sebelumnya
    j = i - 1  
    # Cari posisi yang tepat untuk elemen key
    while j >= 0 and numbers[j] > key:  
        # Geser elemen ke kanan untuk memberikan tempat
        numbers[j+1] = numbers[j]  
        j -= 1  
    # Tempatkan elemen key pada posisi yang benar
    numbers[j+1] = key  

# Menampilkan list setelah diurutkan
print("Array Setelah Sorting: ", numbers)

# Insertion Sort memiliki kompleksitas waktu:
# - Kasus Terburuk: O(n^2)
# - Kasus Terbaik: O(n) (jika array sudah terurut)
# - Rata-rata: O(n^2)
# Algoritma ini menggunakan kompleksitas ruang O(1).
