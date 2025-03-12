#TODO solve the problem in O(log(n))

from typing import List
import bisect

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        neg_count = bisect.bisect_left(nums, 0)  # Index of first non-negative number
        pos_count = len(nums) - bisect.bisect_right(nums, 0)  # Count of positive numbers
        return max(neg_count, pos_count)

if __name__ == "__main__":
    # Hardcoded input
    nums = [-3, -2, -1, 0, 0, 1, 2, 3]  

    solution = Solution()
    print("Maximum Count of Negatives or Positives:", solution.maximumCount(nums))
