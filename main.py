numbers = [64, 34, 25, 12, 22, 11, 90]

#  SORTING ALGORITHMS
#  BUBBLE SORT
def bubble_sort(arr):
  print("Bubble Sort".center(50))
  print("Array Sebelum Sorting: ", arr)
  n = len(arr)
  for i in range(n-1):
    for j in range(n - 1 - i):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
  
  print("Array Setelah Sorting: ", arr, end="\n\n")
  return arr


#  INSERTION SORT
def insertion_sort(arr):
  print("Insertion Sort".center(50))
  print("Array Sebelum Sorting: ", arr)
  n = len(arr)
  for i in range(1, n):
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > key:
      arr[j+1] = arr[j]
      j -= 1
    arr[j+1] = key

  print("Array Setelah Sorting: ", arr, end="\n\n")

  return arr

# SELECTION SORT
def selection_sort(arr):
  print("Selection Sort".center(50))
  print("Array Sebelum Sorting: ", arr)
  n = len(arr)
  for i in range(n-1):
    min_index = i
    for j in range(i+1, n):
      if arr[j] < arr[min_index]:
        min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]
  print("Array Setelah Sorting: ", arr, end="\n\n")
  
  return arr


# SEARCHING ALGORITHMS
# Linear Search / Sequential Search
def linear_search(arr, search):
    n = len(arr)
    found = False
    print(f"Daftar Angka : {arr}")
    for i in range(n):
        if arr[i] == search:
            found = True
            break
    print(f"Angka ditemukan di index ke-{i}" if found else "Angka tidak ditemukan")

# Binary Search
def binary_search(arr, search):
    bubble_sort(arr)
    n = len(arr)
    found = False
    print(f"Daftar Angka : {arr}")
    low = 0
    high = len(arr) - 1
    mid = None
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == search:
            found = True
            break
        elif arr[mid] < search:
            low = mid + 1
        else:
            high = mid - 1
    print(f"Angka ditemukan di index ke-{mid}" if found else "Angka tidak ditemukan")
