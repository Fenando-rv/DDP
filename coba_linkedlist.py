class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # 1. INSERT AFTER (Sudah ada di kode kamu)
    def insert_after(self, prev_data, new_data):
        current = self.head
        while current:
            if current.data == prev_data:
                new_node = Node(new_data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        print(f"Node {prev_data} tidak ditemukan.")

    # 2. INSERT BEFORE
    def insert_before(self, target_data, new_data):
        if self.head is None:
            print("List kosong.")
            return

        # Jika target ada di head (awal)
        if self.head.data == target_data:
            self.add_at_beginning(new_data)
            return

        current = self.head
        while current.next:
            if current.next.data == target_data:
                new_node = Node(new_data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        print(f"Node {target_data} tidak ditemukan.")

    # 3. UPDATE
    def update(self, old_data, new_data):
        current = self.head
        while current:
            if current.data == old_data:
                current.data = new_data
                return
            current = current.next
        print(f"Node {old_data} tidak ditemukan untuk diupdate.")

    # 4. DELETE
    def delete(self, key):
        current = self.head

        # Jika node yang akan dihapus adalah head
        if current is not None:
            if current.data == key:
                self.head = current.next
                current = None
                return

        # Mencari node yang akan dihapus sambil menyimpan node sebelumnya
        prev = None
        while current is not None:
            if current.data == key:
                break
            prev = current
            current = current.next

        if current is None:
            print(f"Node {key} tidak ditemukan untuk dihapus.")
            return

        prev.next = current.next
        current = None

    # 5. SEARCHING
    def search(self, key):
        current = self.head
        position = 0
        while current:
            if current.data == key:
                print(f"Data {key} ditemukan pada indeks ke-{position}.")
                return True
            current = current.next
            position += 1
        print(f"Data {key} tidak ditemukan.")
        return False

    def traverse(self):
        current = self.head
        if not current:
            print("List kosong.")
            return
        while current:
            print(current.data, end=" -> " if current.next else "")
            current = current.next
        print()