from typing import List
from collections import deque

# The most efficient solution by BFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        M, N = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        island_count = 0

        def bfs(m, n):
            queue = deque([(m, n)])
            grid[m][n] = '0'  # Mark as visited
            while queue:
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < M and 0 <= ny < N and grid[nx][ny] == '1':
                        queue.append((nx, ny))
                        grid[nx][ny] = '0'  # Mark visited immediately

        for m in range(M):
            for n in range(N):
                if grid[m][n] == '1':  # Found an island
                    island_count += 1
                    bfs(m, n)

        return island_count

class Solution_DFS:
    def __init__(self):
        self.memo = None
        self.M, self.N = None, None
        self.grid = None

    def find_island_area(self, m, n, mapp):
        if self.memo[m][n] or self.grid[m][n] == '0':
            return 

        self.memo[m][n] = 1  # Mark visited
        mapp.append((m, n))

        if m+1 < self.M:
            self.find_island_area(m+1, n, mapp)
        if n+1 < self.N:
            self.find_island_area(m, n+1, mapp)
        if m-1 >= 0:
            self.find_island_area(m-1, n, mapp)
        if n-1 >= 0:
            self.find_island_area(m, n-1, mapp)

    def numIslands(self, grid: List[List[str]]) -> int:
        self.M, self.N = len(grid), len(grid[0])
        self.memo = [[0] * self.N for _ in range(self.M)]
        self.grid = grid

        island_maps = []
        for m in range(self.M):
            for n in range(self.N):
                if grid[m][n] == '1' and not self.memo[m][n]:
                    mapp = []
                    self.find_island_area(m, n, mapp)
                    island_maps.append(mapp)
                            
        return len(island_maps)

if __name__ == "__main__":
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    
    solution = Solution()
    print(solution.numIslands(grid))  # Expected output: 3
