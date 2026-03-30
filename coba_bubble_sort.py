def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]

# Contoh penggunaan
data = input("Masukkan data array (pisahkan angka dengan spasi): ")
data = list(map(int, data.split()))  # Mengonversi string input menjadi list integer

print("Array sebelum diurutkan:")
print(data)

bubble_sort(data)

print("Array setelah diurutkan menggunakan Bubble Sort:")
print(data)
