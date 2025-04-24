# Solving the problem - https://neetcode.io/problems/islands-and-treasure
from typing import List
from collections import deque


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        treasures = self.find_treasures(grid)

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    grid[i][j] = self.find_shortest_path(grid, (i, j), treasures)

        return grid

    @staticmethod
    def find_treasures(grid: List[List[int]]) -> List[tuple[int, int]]:
        return [(i, j) for i, row in enumerate(grid) for j, val in enumerate(row) if val == 0]

    def find_shortest_path(self, grid: List[List[int]], start: tuple[int, int], treasures: List[tuple[int, int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque([(start[0], start[1], 0)])
        visited = {start}

        while queue:
            x, y, dist = queue.popleft()

            if (x, y) in treasures:
                return dist

            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != -1 and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny, dist + 1))

        return float('inf')


# Further optimized
class Solution2:
    def islandsAndTreasure(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        INF = 2147483647
        queue = deque()

        # 1. Collect all treasure chests
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append((i, j))

        # 2. Multi-source BFS
        while queue:
            x, y = queue.popleft()
            for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == INF:
                    grid[nx][ny] = grid[x][y] + 1
                    queue.append((nx, ny))

        return grid

if __name__ == "__main__":
    grid = [
        [2147483647, -1, 0, 2147483647],
        [2147483647, 2147483647, 2147483647, -1],
        [2147483647, -1, 2147483647, -1],
        [0, -1, 2147483647, 2147483647]
    ]
    solution = Solution()
    import time
    start_time = time.time()
    result = solution.islandsAndTreasure(grid)
    end_time = time.time()
    print(f"Result: {result}")
    print(f"Time taken: {end_time - start_time:.6f} seconds")