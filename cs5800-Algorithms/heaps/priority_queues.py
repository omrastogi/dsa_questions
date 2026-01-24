from heap_array_implementation import Heap

class PriorityQueue(Heap):
    def __init__(self, arr=[]):
        super().__init__()
        if arr:
            self.build_max_heap(arr)
    
    def max_heap_maximum(self):
        if self.heap_size < 1:
            print("heap underflow")
        return self.A[0]

    def max_heap_extract_max(self):
        max = self.max_heap_maximum()
        self.A[1] = self.A[self.heap_size]
        self.heap_size -= 1 
        self.max_heapify(0)
        return max 
    
    def max_heap_increase_key(self, )


            


