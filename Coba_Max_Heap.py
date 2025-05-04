class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._percolate_up(len(self.heap) - 1)

    def _percolate_up(self, index):
        parent_index = (index - 1) // 2
        if index <= 0:
            return
        if self.heap[parent_index] < self.heap[index]:
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            self._percolate_up(parent_index)

    def extract_max(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._percolate_down(0)
        return max_value

    def _percolate_down(self, index):
        left_index = 2 * index + 1
        right_index = 2 * index + 2
        largest = index
        if left_index < len(self.heap) and self.heap[left_index] > self.heap[largest]:
            largest = left_index
        if right_index < len(self.heap) and self.heap[right_index] > self.heap[largest]:
            largest = right_index
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._percolate_down(largest)

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

max_heap = MaxHeap()

# Inserting elements into Max Heap
elements = [50, 30, 40, 10, 20, 35, 25]
for element in elements:
    max_heap.insert(element)

print("Max Heap:")
print(max_heap)

# Extracting maximum element from Max Heap
max_extracted = max_heap.extract_max()
print("\nExtracted Max from Max Heap:", max_extracted)
