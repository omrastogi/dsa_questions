
class MaxHeaps:
    def __init__(self, arr=None):
        self.heap = []
        if arr:
            self.heap = list(arr)
            self.size = len(arr)

    def left(self, i):
        return 2 * i + 1
    
    def right(self, i):
        return 2 * i + 2
    
    def parent(self, i):
        return (i - 1) // 2
    
    def max_heapify(self, i):
        n = self.size
        largest = i
        left = self.left(i)
        right = self.right(i)

        if left < n and self.heap[left] > self.heap[largest]:
            largest = left

        if right < n and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.max_heapify(largest)

    def max_heapify_bottom_up(self, i):
        n = self.size
        smallest = i 
        parent = self.parent(i)
        if i % 2 == 1:
            other_child = i + 1         # if i is odd

        else:
            other_child = i - 1        # if i is even
        
        if self.heap[i] > self.heap[parent]:
            smallest = parent 

        # We assume that the other child is smaller than the parent
        
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.max_heapify_bottom_up(smallest)

    def max_heap_insert(self, value):
        self.heap.append(value)
        self.size += 1
        self.max_heapify_bottom_up(self.size - 1)

    def max_heap_delete(self, i):
        if self.size == 0:
            return None 
        if i < 0 or i >= self.size:
            return None 

        # Replace the element to be deleted with the last element
        self.heap[i], self.heap[self.size - 1] = self.heap[self.size - 1], self.heap[i]
        deleted_value = self.heap.pop()
        self.size -= 1
        self.max_heapify(i)
        return deleted_value

if __name__ == "__main__":
    # Small helper to sanity-check the heap during study
    def is_max_heap(a):
        n = len(a)
        for i in range(n // 2):
            l, r = 2*i + 1, 2*i + 2
            if l < n and a[i] < a[l]: return False
            if r < n and a[i] < a[r]: return False
        return True

    existing_heap = [30, 20, 15, 5, 10]
    h = MaxHeaps()
    h.heap = existing_heap.copy()
    h.size = len(existing_heap)

    print("Start:", h.heap, "| valid heap?", is_max_heap(h.heap))

    # Insert demo (sift-up path)
    print("\nInsert 25 (expect sift-up):")
    h.max_heap_insert(25)
    print(" -> After insert:", h.heap, "| valid heap?", is_max_heap(h.heap))

    # Delete an internal node demo (direction chosen automatically)
    print("\nDelete index 2 (value at 2 =", h.heap[2], ")")
    h.max_heap_delete(2)
    print(" -> After delete idx 2:", h.heap, "| valid heap?", is_max_heap(h.heap))

    # Extract-max style demo by deleting the root
    if h.size > 0:
        print("\nDelete root (extract-max style):")
        root_val = h.heap[0]
        h.max_heap_delete(0)
        print(f" -> Removed {root_val}. New heap:", h.heap, "| valid heap?", is_max_heap(h.heap))






