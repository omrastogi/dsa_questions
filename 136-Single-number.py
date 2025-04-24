"""
XOR Properties – Key to this trick:

1. a ^ a = 0        → any number XOR itself becomes 0
2. a ^ 0 = a        → any number XOR 0 stays the same
3. Commutative      → a ^ b == b ^ a
4. Associative      → a ^ (b ^ c) == (a ^ b) ^ c

These properties make XOR ideal for this problem:
When every element appears twice except one,
XORing all elements cancels out the duplicates,
leaving only the unique number.
"""

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result

if __name__ == "__main__":
    sol = Solution()
    input_nums = [0, 1, 2, 1, 2]
    result = sol.singleNumber(input_nums)
    print(f"The single number in {input_nums} is: {result}")
