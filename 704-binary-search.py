from typing import List

# iterative solution ------------------
class Solution0:
    def search(self, nums: List[int], target: int) -> int:
        N = len(nums)
        low, high = 0, N-1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1

        
        return -1

# recursive solution -----------------
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        N = len(nums)
        low, high = 0, N-1
        self.target = target
        return self.binary_search(nums, low, high)
    
    def binary_search(self, arr, low, high):
        mid = (low + high) // 2
        if low > high:
            return -1 
        elif arr[mid] > self.target:
            return self.binary_search(arr, low, mid - 1)
        elif arr[mid] < self.target:
            return self.binary_search(arr, mid + 1, high)
        elif arr[mid] == self.target:
            return mid
        

if __name__ == "__main__":
    obj = Solution()
    nums = [-1,0,3,5,9,12]
    target = 12
    print(obj.search(nums, target))