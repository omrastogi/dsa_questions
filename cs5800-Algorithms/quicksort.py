import random

def partition(A, low, high):
    # this is a two-pointer approach in same space & O(1) extra space
    # define i and j which act as partitioning “markers” between regions
    # - i: the index before which all numbers ≤ pivot are kept
    # - j: scans the array; before each step, all numbers in (i, j) are > pivot
    # pivot at A[high] (the last item)
    pivot = A[high]             # 1. pivot = A[high] | the last item

    i = low - 1                 # 2. i = low - 1
    # since no processing yet, items A[low..i] form the ≤ pivot region (currently empty)
    # and A[i+1..j-1] are assumed > pivot before we process j

    # 3. for j = low to high - 1
    for j in range(low, high):
        # 4. if A[j] ≤ pivot:
        if A[j] <= pivot:
            i += 1              #    increase i pointer (extend the ≤ region)
            # 6. exchange A[i] with A[j]  | shift the lower number into the ≤ region
            A[i], A[j] = A[j], A[i]

    # 7. lastly, bring the pivot to sit between the two partitions
    #    exchange A[i + 1] with A[high]
    A[i + 1], A[high] = A[high], A[i + 1]

    # 8. return i + 1 (final pivot index)
    return i + 1

def quicksort(arr, low, high, randn=False, debug=False, depth=0):
    if low >= high: 
        return arr
    if debug:
        print("To partition", arr)
    if randn:
        p = randomized_partition(arr, low, high)  
    else:
        p = partition(arr, low, high)
    if debug:
        indent = "  " * depth
        print(f"{indent}[low={low}, high={high}] p={p} pivot={arr[p]} | "
          f"left={arr[low:p]} | right={arr[p+1:high+1]}")
    quicksort(arr, low, p-1, randn, debug, depth)
    quicksort(arr, p+1, high, randn, debug, depth)
    return arr

def randomized_partition(arr, low, high):
    k = random.randint(low, high)
    arr[k], arr[high] = arr[high], arr[k]
    return partition(arr, low, high)

    
if __name__ == "__main__":
    print("Best case scenario")
    arr = [2, 1, 4, 7, 3, 6, 5]
    print(quicksort(arr, 0, len(arr)-1, randn=True, debug=1))        
    
    print("Worst case scenario")
    arr = [1, 2, 3, 4, 5, 6, 7]
    print(quicksort(arr, 0, len(arr)-1, randn=True, debug=1))        

    print("Worst case scenario")
    arr = [7, 6, 5, 4, 3, 2, 1]
    print(quicksort(arr, 0, len(arr)-1, randn=True, debug=1))        
