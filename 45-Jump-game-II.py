from typing import List

# REQUIRES PRECISE SOLUTION 

class Solution:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)
        jumps = 0
        curr_end = 0
        curr_farthest = 0
        for i in range(0, N-1):
            curr_farthest = max(curr_farthest,i+nums[i])
            if i == curr_end:
                jumps += 1
                curr_end = curr_farthest

 
        return jumps


if __name__ == "__main__":
    obj = Solution()
    nums = [2,3,1,1,4]
    print(obj.jump(nums))  # Expected: 2
    
    nums = [2,3,0,1,4]
    print(obj.jump(nums))  # Expected: 2
    
    nums = [1]
    print(obj.jump(nums))  # Expected: 0