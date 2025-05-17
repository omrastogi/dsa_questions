# Bubble Sort
class Solution0:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        for i in range(N):
            for j in range(i):
                if nums[j] > nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
                

class Solution:
    def quicksort(self, arr, low, high):
        if low < high:
            p = self.partition(arr, low, high)
            self.quicksort(arr, low, p - 1)   # left part
            self.quicksort(arr, p + 1, high)  # right part
    
    @staticmethod
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1  # boundary for elements < pivot

        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]  # place pivot
        return i + 1  # return pivot's final index


    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # I will be using quicksort and using middle as pivot 
        N = len(nums)
        self.quicksort(nums, 0, N-1)
