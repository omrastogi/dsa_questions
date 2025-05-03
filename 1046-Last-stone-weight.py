import bisect
import heapq
from typing import List

class Solution0:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        N = len(stones)
        for i in range(N-1):
            x, y = stones.pop(), stones.pop()
            new_stone = abs(y - x)
            bisect.insort_left(stones, new_stone)
            # print(stones)
        return stones[-1]


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Use negative numbers to simulate a max-heap
        stones = [-s for s in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            y = -heapq.heappop(stones)
            x = -heapq.heappop(stones)
            if y != x:
                heapq.heappush(stones, -(y - x))
        
        return -stones[0] if stones else 0


if __name__ == "__main__":
    obj = Solution()
    stones = [2,7,4,1,8,1]
    print(obj.lastStoneWeight(stones))
