from typing import List
import time

class Solution:
    def __init__(self):
        self.nums = None 
        self.memo = {}
    
    def rob_house(self, i, sum):
        if i >= len(self.nums):
            return sum
        elif i == len(self.nums)-1:
            return sum + self.nums[i]
        elif i == len(self.nums)-2:
            return sum + self.nums[i]
        else:
            if i in self.memo.keys():
                return self.memo[i]
            sum = max(self.rob_house(i+2, sum), self.rob_house(i+3, sum))
            if i > -1:
                sum += self.nums[i]
                self.memo[i] = sum
        return sum

    def rob(self, nums: List[int]) -> int:
        self.nums = nums
        return self.rob_house(-2, 0)

if __name__ == "__main__":
    solution = Solution()
    nums = [226,174,214,16,218,48,153,131,128,17,157,142,88,43,37,157,43,221,191,68,206,23,225,82,54,118,111,46,80,49,245,63,25,194,72,80,143,55,209,18,55,122,65,66,177,101,63,201,172,130,103,225,142,46,86,185,62,138,212,192,125,77,223,188,99,228,90,25,193,211,84,239,119,234,85,83,123,120,131,203,219,10,82,35,120,180,249,106,37,169,225,54,103,55,166,124] # Hardcoded input
    # nums = [6,6,4,8,4,3,3,10]
    start_time = time.time()
    max_robbed_amount = solution.rob(nums)
    end_time = time.time()
    
    print(f"Maximum amount that can be robbed: {max_robbed_amount}")
    print(f"Time taken: {end_time - start_time} seconds")