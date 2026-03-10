def sequential_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1

# Contoh penggunaan
data = [10, 22, 5, 31, 17]
print(data)

target = int(input("Masukkan data yang dicari = "))

index = sequential_search(data, target)

if index != -1:
    print("Target ditemukan pada indeks:", index)
else:
    print("Target tidak ditemukan dalam daftar.")