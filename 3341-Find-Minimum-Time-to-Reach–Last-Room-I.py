# Dikstra Question 

# Can't be solved by dfs 

import heapq
from typing import List

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        dist = [[float('inf')] * m for _ in range(n)]
        dist[0][0] = 0

        heap = [(0, 0, 0)]  # (time, x, y)
        while heap:
            t, x, y = heapq.heappop(heap)
            if t > dist[x][y]:
                continue
            if (x, y) == (n - 1, m - 1):
                return t

            for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    start = max(t, moveTime[nx][ny])
                    arrive = start + 1
                    if arrive < dist[nx][ny]:
                        dist[nx][ny] = arrive
                        heapq.heappush(heap, (arrive, nx, ny))

        return -1


if __name__ == "__main__":
    obj = Solution()
    
    moveTime = [
        [0, 1, 3],
        [2, 4, 2], 
        [1, 3, 1]
    ]
    print(obj.minTimeToReach(moveTime))  # Expected: 4
    
    moveTime = [
        [0, 2, 4],
        [3, 1, 5],
        [2, 3, 1]
    ] 
    print(obj.minTimeToReach(moveTime))  # Expected: 5
    
    moveTime = [
        [0]
    ]
    print(obj.minTimeToReach(moveTime))  # Expected: 0

