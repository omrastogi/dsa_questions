from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        largst_num = nums[0] - 1
        for i in range(1, N):
            if largst_num < 0:
                return False 
            largst_num = max(largst_num, nums[i]) - 1

        return True


if __name__ == "__main__":
    obj = Solution()
    nums = [2,3,1,1,4]
    print(obj.canJump(nums))  # Expected: True
    
    nums = [3,2,1,0,4] 
    print(obj.canJump(nums))  # Expected: False
    
    nums = [0]
    print(obj.canJump(nums))  # Expected: True