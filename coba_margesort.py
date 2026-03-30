def merge_sort(data):
    if len(data) > 1:
        mid = len(data) // 2
        left_half = data[:mid]
        right_half = data[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # Menggabungkan dua sub-array secara berurutan
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                data[k] = left_half[i]
                i += 1
            else:
                data[k] = right_half[j]
                j += 1
            k += 1

        # Memeriksa apakah masih ada elemen yang tersisa di left_half
        while i < len(left_half):
            data[k] = left_half[i]
            i += 1
            k += 1

        # Memeriksa apakah masih ada elemen yang tersisa di right_half
        while j < len(right_half):
            data[k] = right_half[j]
            j += 1
            k += 1

# Contoh penggunaan
data = input("Masukkan data array (pisahkan angka dengan spasi): ")
data = list(map(int, data.split()))  # Mengonversi string input menjadi list integer

print("Array sebelum diurutkan:")
print(data)

merge_sort(data)
print("Array setelah diurutkan menggunakan Merge Sort:")
print(data)
