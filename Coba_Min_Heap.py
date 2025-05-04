class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._percolate_up(len(self.heap) - 1)

    def _percolate_up(self, index):
        parent_index = (index - 1) // 2
        if index <= 0:
            return
        if self.heap[parent_index] > self.heap[index]:
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            self._percolate_up(parent_index)

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._percolate_down(0)
        return min_value

    def _percolate_down(self, index):
        left_index = 2 * index + 1
        right_index = 2 * index + 2
        smallest = index
        if left_index < len(self.heap) and self.heap[left_index] < self.heap[smallest]:
            smallest = left_index
        if right_index < len(self.heap) and self.heap[right_index] < self.heap[smallest]:
            smallest = right_index
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._percolate_down(smallest)

    def __str__(self):
        return self._print(0, 0)

    def _print(self, index, level):
        if index >= len(self.heap):
            return ""
        result = ""
        result += self._print(2 * index + 2, level + 1)
        result += "\n" + "    " * level + str(self.heap[index])
        result += self._print(2 * index + 1, level + 1)
        return result


# Example usage:

min_heap = MinHeap()

# Inserting elements into Min Heap
elements = [10, 20, 15, 30, 25, 40, 35]
for element in elements:
    min_heap.insert(element)

print("Min Heap:")
print(min_heap)

# Extracting minimum element from Min Heap
min_extracted = min_heap.extract_min()
print("\nExtracted Min from Min Heap:", min_extracted)
