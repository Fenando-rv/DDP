class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self): 
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]

    def size(self):
        return len(self.items)

    def display(self):
        return self.items

    def count(self, item):
        #Menghitung jumlah kemunculan item dalam stack
        return self.items.count(item)

    def change(self, index, new_item):
        #Mengubah nilai item pada indeks tertentu dalam stack
        if 0 <= index < len(self.items):
            self.items[index] = new_item
        else:
            print("Indeks di luar jangkauan!")

# Contoh penggunaan