class PriorityQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, item, priority):
        self.items.append((item, priority))
        self.items.sort(key=lambda x: x[1])  # Urutkan berdasarkan prioritas

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)[0]

    def peek(self):
        if not self.is_empty():
            return self.items[0][0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
    
    def display_all(self):
        # Menampilkan seluruh elemen dalam queue
        if not self.is_empty():
            for item, priority in self.items:
                print(f"Item: {item}, Prioritas: {priority}")
        else:
            print("Queue kosong.")
#Coba Penggunaan
