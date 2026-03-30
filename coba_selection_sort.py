def selection_sort(data):
    n = len(data)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if data[j] < data[min_idx]:
                min_idx = j
                
        # Tukar elemen terkecil yang ditemukan dengan elemen pertama
        data[i], data[min_idx] = data[min_idx], data[i]

# Contoh penggunaan
data = input("Masukkan data array (pisahkan angka dengan spasi): ")
data = list(map(int, data.split()))  # Mengonversi string input menjadi list integer

print("Array sebelum diurutkan:")
print(data)

selection_sort(data)

print("Array setelah diurutkan menggunakan Selection Sort:")
print(data)
