def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key

# Contoh penggunaan
data = input("Masukkan data array (pisahkan angka dengan spasi): ")
data = list(map(int, data.split()))  # Mengonversi string input menjadi list integer

print("Array sebelum diurutkan:")
print(data)
insertion_sort(data)
print("Array setelah diurutkan menggunakan Insertion Sort:")
print(data)
