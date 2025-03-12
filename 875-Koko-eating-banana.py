import math
from typing import List

class Solution:
    def check_hours(self, piles: List[int], k: int) -> int:
        """Returns the total hours required to eat all piles at speed k."""
        return sum(math.ceil(pile / k) for pile in piles)

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """Finds the minimum eating speed `k` that allows finishing all bananas in `h` hours."""
        i, j = 1, max(piles) + 1  # Search space for k
        while i < j:
            mid = (i + j) // 2
            if self.check_hours(piles, mid) > h:
                i = mid + 1  # Need a larger `k` to eat faster
            else:
                j = mid  # Could be an answer, try smaller `k`
        
        return i  # `i` now holds the minimum k

if __name__ == "__main__":
    # Hardcoded input
    piles = [3, 6, 7, 11]
    h = 8

    # Running the solution
    solution = Solution()
    print("Minimum Eating Speed:", solution.minEatingSpeed(piles, h))
