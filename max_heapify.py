def max_heapify(heap, i):
    n = len(heap)
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and heap[left] > heap[largest]:
        largest = left
    if right < n and heap[right] > heap[largest]:
        largest = right

    if largest != i:
        heap[i], heap[largest] = heap[largest], heap[i]
        max_heapify(heap, largest)

def max_heapify_iterative(heap, i):
    n = len(heap)
    while True:
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and heap[left] > heap[largest]:
            largest = left
        if right < n and heap[right] > heap[largest]:
            largest = right

        if largest != i:
            heap[i], heap[largest] = heap[largest], heap[i]
            i = largest
        else:
            break

def build_max_heap(heap):
    n = len(heap)
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(heap, i)

# Example input
heap = [3, 5, 1, 8, 7, 2]
build_max_heap(heap)
print("Max Heap:", heap)
