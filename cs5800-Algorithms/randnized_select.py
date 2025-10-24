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

def randomized_partition(arr, low, high):
    k = random.randint(low, high)
    arr[k], arr[high] = arr[high], arr[k]
    return partition(arr, low, high)

def quick_select(arr, low, high, idx, debug=False, _depth=0):
    if debug:
        print(f"[QS] depth={_depth} range=[{low},{high}] idx={idx} sub={arr[low:high+1]}")

    if low == high:
        return arr[low]
    pivot = randomized_partition(arr, low, high)
    rank_in_subarray = pivot - low + 1

    if debug:
        print(f"[QS] depth={_depth} pivot_index={pivot} pivot_val={arr[pivot]} "
              f"rank_in_subarray={rank_in_subarray}")
        
    if idx == rank_in_subarray:
        return arr[pivot]
    elif idx < rank_in_subarray:
        if debug:
            print(f"[QS] depth={_depth} go LEFT (keep idx={idx})")
        return quick_select(arr, low, pivot-1, idx, debug, _depth+1)
    else:
        if debug:
            print(f"[QS] depth={_depth} go RIGHT (shift idx to {idx - rank_in_subarray})")
        return quick_select(arr, pivot+1, high, idx-rank_in_subarray, debug, _depth+1)
    
def quick_select_iterative(arr, low, high, idx):
    while low < high:
        # random pivot -> end
        k = random.randint(low, high)
        arr[k], arr[high] = arr[high], arr[k]

        # in-place partition using only idx,j and the pivot-at-end
        x, p = arr[high], low-1
        for j in range(low, high):
            if arr[j] <= x:
                p += 1 
                arr[p], arr[j] = arr[j], arr[p]
        
        # final pivot position 
        pivot = p + 1 
        arr[pivot], arr[high] = arr[high], arr[pivot]
        rank = pivot - low + 1 # pivot rank within current window
        if idx == rank:
            return arr[pivot]
        elif idx < rank:
            h = pivot -1 
        else:
            low = pivot + 1 
            idx -= rank 
    return arr[low]
    
    
if __name__ == "__main__":
    # Demo usage
    random.seed(42)  # for reproducibility

    data = [9, 3, 7, 1, 5, 8, 2, 6, 4, 5]  # sample array (with duplicate 5)
    n = len(data)

    # Example 1: find the 4th smallest (1-indexed)
    idx = 4
    arr1 = data[:]  # copy since quick_select mutates the array
    print(f"Array: {arr1}")
    result = quick_select(arr1, 0, n - 1, idx, debug=True)
    print(f"\n{idx}-th smallest = {result}\n")

    # Example 2: find the 2nd largest by converting to k-th smallest
    # 2nd largest == (n - 2 + 1)-th smallest
    kth_smallest_for_2nd_largest = n - 2 + 1
    arr2 = data[:]
    second_largest = quick_select_iterative(arr2, 0, n - 1, kth_smallest_for_2nd_largest)
    print(f"2nd largest = {second_largest}")

    # Verification against full sort
    print(f"Sorted check: {sorted(data)}")
