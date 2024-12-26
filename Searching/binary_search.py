# Bubble Sort Algorithm
def bubble_sort(arr):
    """Mengurutkan array menggunakan Bubble Sort"""
    print("Bubble Sort".center(50))
    print("Array Sebelum Sorting: ", arr)
    n = len(arr)
    for i in range(n-1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print("Array Setelah Sorting: ", arr)
    return arr

# Binary Search Algorithm
def binary_search(arr, target):
    """Mencari angka menggunakan Binary Search"""
    low = 0
    high = len(arr) - 1
    while low <= high:
        # Hitung nilai tengah
        mid = (low + high) // 2
        # Jika target ditemukan
        if arr[mid] == target:
            return mid
        # Jika target lebih besar, cari di sisi kanan
        elif arr[mid] < target:
            low = mid + 1
        # Jika target lebih kecil, cari di sisi kiri
        else:
            high = mid - 1
    # Jika target tidak ditemukan
    return -1

# List yang kita miliki
numbers = [1, 5, 3, 2, 6, 4, 7]

# Sorting terlebih dahulu
bubble_sort(numbers)

# Input angka yang dicari
search = int(input("Ingin cari angka berapa? "))

# Lakukan pencarian menggunakan Binary Search
result = binary_search(numbers, search)

# Tampilkan hasil pencarian
if result != -1:
    print(f"Angka {search} ditemukan di index ke-{result}")
else:
    print(f"Angka {search} tidak ditemukan dalam list")

# Kompleksitas waktu:
# - Best case: O(1), jika angka ditemukan di tengah.
# - Average/Worst case: O(log n), karena rentang pencarian berkurang separuh setiap iterasi.
