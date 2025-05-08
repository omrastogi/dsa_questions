import heapq
from typing import List

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        INF = float('inf')
        # dist[i][j][par]: min time to reach (i,j) when the next move cost parity is par (0 → cost=1, 1 → cost=2)
        dist = [[[INF] * 2 for _ in range(m)] for _ in range(n)]
        dist[0][0][0] = 0

        # priority queue entries: (time, i, j, parity)
        pq = [(0, 0, 0, 0)]
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while pq:
            time, i, j, par = heapq.heappop(pq)
            if time != dist[i][j][par]:
                continue
            if i == n - 1 and j == m - 1:
                return time

            move_cost = 1 if par == 0 else 2
            for dx, dy in dirs:
                ni, nj = i + dx, j + dy
                if 0 <= ni < n and 0 <= nj < m:
                    # wait until the room is open
                    depart = max(time, moveTime[ni][nj])
                    arrival = depart + move_cost
                    npar = par ^ 1
                    if arrival < dist[ni][nj][npar]:
                        dist[ni][nj][npar] = arrival
                        heapq.heappush(pq, (arrival, ni, nj, npar))

        return -1


if __name__ == "__main__":
    obj = Solution()
    
    moveTime = [
        [0, 1, 3],
        [2, 4, 2],
        [1, 3, 1]
    ]
    print(obj.minTimeToReach(moveTime))  # Expected: 5
    
    moveTime = [
        [0, 2, 4],
        [3, 1, 5], 
        [2, 3, 1]
    ]
    print(obj.minTimeToReach(moveTime))  # Expected: 6
    
    moveTime = [
        [0]
    ]
    print(obj.minTimeToReach(moveTime))  # Expected: 0

