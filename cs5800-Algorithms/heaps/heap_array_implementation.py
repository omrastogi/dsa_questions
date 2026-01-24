class Heap:
    def __init__(self, heap=[]):
        self.A = heap
        self.heap_size = len(heap)

    def parent(self, i):
        return (i - 1) // 2
    
    def left(self, i):
        return 2*i + 1

    def right(self, i):
        return 2*i + 2

    def max_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
    
        if l <= self.heap_size and self.A[l] > self.A[i]:
            largest = l 
        else:
            largest = i
        
        if r <= self.heap_size and self.A[r] > self.A[largest]:
            largest = r 
        
        if largest != i:
            self.A[i], self.A[largest] = self.A[largest], self.A[i]
            self.max_heapify(largest)
    
    def check_max_heap(self):
        if not self.A:
            return None
        
        for i in self.range(0, self.heap_size//2):
            l = self.left(i)
            r = self.right(i)
            if self.A[l] > self.A[i] or self.A[r] > self.A[i]:
                return False
        
        return True
    
    def build_max_heap(self, arr, n):
        """
        Assumption:
        This function assumes that there is not existing heap and take a list of number
        
        Input: 
            arr: unordered list of n numbers
            n  : length of list arr
        """
        self.A = arr
        self.heap_size = n
        # no point in running max_heapify on leaf i.e. after n//2
        for i in range(n//2 - 1, -1, -1):
            self.max_heapify(i)


if __name__ == "__main__":
    h = Heap()
    h.build_max_heap([1,4,5,2,3,6], n=5)
    print(h.A)