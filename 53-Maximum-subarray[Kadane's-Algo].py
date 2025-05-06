from typing import List

class Solution0:
    def maxSubArray(self, nums: List[int]) -> int:
        def helper(left: int, right: int) -> int:
            if left == right:
                return nums[left]
            
            mid = (left + right) // 2
            left_sum = helper(left, mid)
            right_sum = helper(mid + 1, right)
            cross_sum = max_crossing_sum(nums, left, mid, right)
            
            return max(left_sum, right_sum, cross_sum)
        
        def max_crossing_sum(nums: List[int], left: int, mid: int, right: int) -> int:
            left_max = float('-inf')
            total = 0
            for i in range(mid, left - 1, -1):
                total += nums[i]
                left_max = max(left_max, total)
            
            right_max = float('-inf')
            total = 0
            for i in range(mid + 1, right + 1):
                total += nums[i]
                right_max = max(right_max, total)
            
            return left_max + right_max
        
        return helper(0, len(nums) - 1)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_num = max(nums)
        if max_num < 0:
            return max_num
        local_sum, global_sum = 0, 0 
        for num in nums:
            local_sum += num
            if local_sum<0:
                local_sum = 0 
            global_sum = max(global_sum, local_sum)
        return global_sum 




if __name__ == "__main__":
    obj = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(obj.maxSubArray(nums))  # Expected: 6
    
    nums = [1]
    print(obj.maxSubArray(nums))  # Expected: 1
    
    nums = [5,4,-1,7,8]
    print(obj.maxSubArray(nums))  # Expected: 23
