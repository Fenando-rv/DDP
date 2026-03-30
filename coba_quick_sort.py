def quick_sort(data):
    if len(data) <= 1:
        return data
    else:
        pivot = data[0]
        less_than_pivot = [x for x in data[1:] if x <= pivot]
        greater_than_pivot = [x for x in data[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

# Contoh penggunaan
data = input("Masukkan data array (pisahkan angka dengan spasi): ")
data = list(map(int, data.split()))  # Mengonversi string input menjadi list integer

print("Array sebelum diurutkan:")
print(data)

data = quick_sort(data)
print("Array setelah diurutkan menggunakan Quicksort:")
print(data)
