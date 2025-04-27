from typing import List

class KthLargest0:
    def __init__(self, k: int, nums: List[int]):
        self.k = k 
        self.nums = nums
        self.nums.sort(reverse=True)
        self.N = len(self.nums)

    def add(self, val: int) -> int:
        new_list = []
        inserted = False  # new flag to track insertion
        
        if not self.nums:
            new_list.append(val)
            inserted = True
        else:
            for i in range(self.N):
                if not inserted and val >= self.nums[i]:
                    new_list.append(val)
                    inserted = True
                new_list.append(self.nums[i])
            
            if not inserted:
                new_list.append(val)
        
        self.nums = new_list
        self.N += 1
        return self.nums[self.k-1]
                    
# My implementation using binary tree
class KthLargest1:
    def __init__(self, k: int, nums: List[int]):
        self.k = k 
        self.nums = nums
        self.nums.sort(reverse=True)
        self.N = len(self.nums)

    def add(self, val: int) -> int:
        i, j = 0, self.N - 1 
        if self.nums == []:
            self.nums.append(val) 
        elif self.nums[i] <= val:
            self.nums.insert(0, val)
        elif self.nums[j] >= val:
            self.nums.append(val) 
        else:
            while i<j:
                mid = (i+j) // 2
                if val <= self.nums[mid] and val >= self.nums[mid+1]:
                    self.nums.insert(mid+1, val)
                    break
                elif self.nums[mid]<val:
                    j = mid 
                else:
                    i = mid
        
        self.N += 1
        return self.nums[self.k-1]

# Heap + Binary Search
import heapq
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)  # O(N)
        while len(self.heap) > k:
            heapq.heappop(self.heap)  # Remove smallest elements

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)  # Add new value
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)    # Remove smallest if more than k elements
        return self.heap[0]  # kth largest is the smallest in heap


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
if __name__ == "__main__":
    # Original test case
    k = 3
    nums = [4, 5, 8, 2]
    kthLargest = KthLargest(k, nums)
    print(kthLargest.add(3))   # expect 4
    print(kthLargest.add(5))   # expect 5
    print(kthLargest.add(10))  # expect 5
    print(kthLargest.add(9))   # expect 8
    print(kthLargest.add(4))   # expect 8

    # Additional test case: [[4,[7,7,7,7,8,3]],[2],[10],[9],[9]]
    k2 = 4
    nums2 = [7, 7, 7, 7, 8, 3]
    kthLargest2 = KthLargest(k2, nums2)
    print(kthLargest2.add(2))   # output depends on implementation
    print(kthLargest2.add(10))
    print(kthLargest2.add(9))
    print(kthLargest2.add(9))
    
    # Test case: [[1,[]],[-3],[-2],[-4],[0],[4]]
    k3 = 1
    nums3 = []
    kthLargest3 = KthLargest(k3, nums3)
    print(kthLargest3.add(-3))  # expect -3
    print(kthLargest3.add(-2))  # expect -2
    print(kthLargest3.add(-4))  # expect -2
    print(kthLargest3.add(0))   # expect 0
    print(kthLargest3.add(4))   # expect 4
