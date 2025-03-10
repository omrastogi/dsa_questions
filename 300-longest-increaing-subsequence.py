from typing import List

# This is was practice run -- Dynamic Programming
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = [1]*len(nums)
        answer = 1 
        for i in range(len(nums)):
            for left in range(i):
                if nums[left] < nums[i]:
                    if lis[left]+1 > lis[i]:
                        lis[i] = lis[left] + 1
            answer = max(answer, lis[i])
        return answer
    
# The most optimised solution - Binary Search with Greedy Algo (with dp like strategy)
class Solution:
    def __init__(self):
        self.monotonic = []

    def bisect_left(self, arr, target):
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2 
            if arr[mid] < target:
                left = mid + 1 
            else:
                right = mid 
        return left   

    def lengthOfLIS(self, nums: List[int]) -> int:
        monotonic = []

        for num in nums:
            idx = self.bisect_left(self.monotonic, num)
            if idx == len(self.monotonic):
                self.monotonic.append(num)
            else:
                self.monotonic[idx] = num 
            print(self.monotonic)

        return len(self.monotonic) 


