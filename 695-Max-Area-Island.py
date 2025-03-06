from typing import List
from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0  
        
        M, N = len(grid), len(grid[0])
        directions  = [(1,0), (-1,0), (0,1), (0,-1)]
        largest_area = 0

        def bfs(m, n):
            queue = deque([(m,n)])
            grid[m][n] = 0 # Mark as visited
            area = 0
            while queue:
                x, y = queue.popleft()
                area += 1
                for dx, dy in directions:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < M and 0 <= ny < N and grid[nx][ny]:
                        queue.append((nx, ny))
                        grid[nx][ny] = 0 # Mark as visted
            
            return area


        for m in range(M):
            for n in range(N):
                if grid[m][n]:
                    area = bfs(m, n)
                    largest_area = max(largest_area, area)
        
        return largest_area

if __name__ == "__main__":
    grid = [
        [0,0,1,0,0,0,1,1,0,1],
        [1,1,1,0,1,0,1,1,0,1],
        [0,0,0,0,1,1,0,0,0,0],
        [1,1,1,0,0,1,1,1,0,0],
        [0,0,0,1,1,1,0,0,1,1],
        [1,1,0,0,0,1,1,1,1,0]
    ]
    
    solution = Solution()
    print("Largest island area:", solution.maxAreaOfIsland(grid))


