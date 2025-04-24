from collections import deque
from typing import List, Tuple


class Solution0:
    def __init__(self):
        self.memos = {}

    def dfs(self, m: int, n: int) -> int:
        if m == 0 and n == 0:
            return 1
        if (m, n) in self.memos:
            return self.memos[(m, n)]
        paths = 0
        if m > 0:
            paths += self.dfs(m - 1, n)
        if n > 0:
            paths += self.dfs(m, n - 1)
        self.memos[(m, n)] = paths
        return paths

    def uniquePaths(self, m: int, n: int) -> int:
        return self.dfs(m - 1, n - 1)

# Slow solution 
class Solution1:
    def uniquePaths(self, m: int, n: int) -> int:
        queue: deque[Tuple[int, int]] = deque([(m - 1, n - 1)])
        paths = 0
        while queue:
            m, n = queue.popleft()
            if m == 0 and n == 0:
                paths += 1
                continue
            if m > 0:
                queue.append((m - 1, n))
            if n > 0:
                queue.append((m, n - 1))

        return paths

# This has to be the most intuitive solution and most efficient one 
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1]*n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
        return dp[m-1][n-1]


if __name__ == "__main__":
    sol = Solution()
    test_cases: List[Tuple[int, int]] = [
        (4, 3)
    ]

    for m, n in test_cases:
        result = sol.uniquePaths(m, n)
        print(f"Number of unique paths for {m}x{n} grid: {result}")
