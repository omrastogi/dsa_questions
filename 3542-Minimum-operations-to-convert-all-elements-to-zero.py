from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        stack = []
        opr = 0

        for num in nums:
            while stack and stack[-1] > num:
                stack.pop()
            if num > 0 and (not stack or stack[-1] < num):
                stack.append(num)
                opr += 1

        return opr
    
if __name__ == "__main__":
    nums1 = [0, 2]  # Basic test case
    nums2 = [3, 1, 2, 1]  # Test case with duplicates
    nums3 = [1, 2, 1, 2, 1, 2]  # Test case with alternating numbers
    nums4 = [4, 1, 6, 4]  # Edge case: max length array with all zeros
    nums5 = [0, 0, 0, 0]  # Edge case: all zeros
    nums6 = [1, 1, 1, 1]  # Edge case: all same numbers
    nums7 = [1, 2, 3, 4]  # Edge case: strictly increasing

    solution = Solution()
    print(solution.minOperations(nums1))
    print(solution.minOperations(nums2))
    print(solution.minOperations(nums3))
    print(solution.minOperations(nums4))
    print(solution.minOperations(nums5))
    print(solution.minOperations(nums6))
    print(solution.minOperations(nums7))