import random

def partition(arr, low, high):
    pivot = arr[high] 
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]    
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

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
