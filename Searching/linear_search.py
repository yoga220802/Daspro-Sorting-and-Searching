# Linear Search Algorithm
# Algoritma ini bekerja dengan memeriksa setiap elemen pada list secara berurutan.
# Jika elemen yang dicari ditemukan, algoritma berhenti.

# Array yang kita miliki
numbers = [1, 5, 3, 2, 6, 4, 7]

# Hitung jumlah elemen dalam list
n = len(numbers)

# Status awal pencarian angka
found = False

# Inisialisasi index hasil pencarian
index = None

# Tampilkan daftar angka
print(f"Daftar Angka: {numbers}")

# Input angka yang dicari
search = int(input("Ingin cari angka berapa? "))

# Langkah 1: Lakukan pencarian menggunakan linear search
for i in range(n):
    # Jika angka dalam list sama dengan angka yang dicari
    if numbers[i] == search:
        # Ubah status found menjadi True
        found = True
        # Simpan index elemen yang ditemukan
        index = i
        # Hentikan perulangan
        break

# Langkah 2: Tampilkan hasil pencarian
if found:
    print(f"Angka {search} ditemukan di index ke-{index}")
else:
    print(f"Angka {search} tidak ditemukan dalam list")

# Kompleksitas waktu:
# - Worst case: O(n), ketika elemen berada di akhir atau tidak ada dalam list.
# - Best case: O(1), ketika elemen ditemukan di awal.
