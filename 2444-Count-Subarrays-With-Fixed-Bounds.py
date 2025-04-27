from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        res = 0
        last_bad = last_max = last_min = -1
        for i, num in enumerate(nums):
            if num > maxK or num < minK:
                last_bad = i
            if num == maxK:
                last_max = i
            if num == minK:
                last_min = i
            res += max(0, min(last_min, last_max) - last_bad)
        return res


if __name__ == "__main__":
    nums = [1, 3, 5, 2, 7, 5]
    minK = 1
    maxK = 5
    sol = Solution()
    print(sol.countSubarrays(nums, minK, maxK))
