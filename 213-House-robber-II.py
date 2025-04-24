from typing import List
import time

class Solution:
    def rob_linear(self, nums: List[int]) -> int:
        memo = {}
        def dp(i: int) -> int:
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]
            memo[i] = max(dp(i + 1), nums[i] + dp(i + 2))
            return memo[i]
        return dp(0)

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)
        # Rob 0 to n-2 or 1 to n-1
        return max(self.rob_linear(nums[:-1]), self.rob_linear(nums[1:]))

if __name__ == "__main__":
    solution = Solution()
    nums = [4, 1, 2, 7, 5, 3, 1]
    start_time = time.time()
    max_robbed_amount = solution.rob(nums)
    end_time = time.time()

    print(f"Maximum amount that can be robbed: {max_robbed_amount}")
    print(f"Time taken: {end_time - start_time:.6f} seconds")
